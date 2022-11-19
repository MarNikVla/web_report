import pathlib

from django.core.exceptions import EmptyResultSet
from django.core.files.storage import default_storage
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse

from django.views import View
from django.views.generic import TemplateView

from web_report_card.main import make_file_for_web_app

IN_SESSION_FILE_KEY = 'uploaded_file'

class HomeView(TemplateView):
    template_name = 'web_report_card/main.html'

class NotCorrectFileUploadView(TemplateView):
    template_name = 'web_report_card/errors.html'

class TestView(TemplateView):
    template_name = 'web_report_card/test.html'

    def make_result(self, file_name):
        try:
            return make_file_for_web_app(file_name)
        except:
            raise Http404

    def get(self, request, *args, **kwargs):
        if IN_SESSION_FILE_KEY in request.session:
            file = request.session[IN_SESSION_FILE_KEY]
            file_name = default_storage.save(file.name, file)
            del request.session[IN_SESSION_FILE_KEY]
            result_file_path = self.make_result(file_name)
            request.session['result_file_path'] = result_file_path
            return super(TestView, self).get(request, *args, **kwargs)
        else:
            # return HttpResponse('Загрузите корректный файл')
            # return HttpResponseServerError("dff")
            return HttpResponseRedirect(reverse('web_report_card:not_correct_file_upload'))


def file_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        request.session[IN_SESSION_FILE_KEY] = file
    return HttpResponse('Done!')


class FileDownloadView(View):

    content_type_value_xlsx = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def get(self, request, *args, **kwargs):
        if 'result_file_path' in request.session:
            file_path = request.session['result_file_path']
            file = default_storage.open(file_path)
            result_file_path_obj = pathlib.Path(file.name)
            with file as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value_xlsx
                )
                response['Content-Disposition'] = 'attachment; filename=' + result_file_path_obj.name
            del request.session['result_file_path']
            result_file_path_obj.unlink(missing_ok=True)
            return response
        else:
            raise Http404
