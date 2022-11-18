from django.core.files.storage import default_storage
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin, FormView

from web_report_card.forms import DocumentForm, DocumentFormDrop
from web_report_card.main import save_file, save_file_for_web
from web_report_card.models import Document


class HomeView(TemplateView):
    template_name = 'web_report_card/main.html'




class TestView(TemplateView):

    template_name = 'web_report_card/test.html'

    def make_result(self, file_name):
        result = save_file_for_web(file_name)
        return result


    def get(self, request, *args, **kwargs):
        print('grafik' in request.session)
        if 'grafik' in request.session:
            print('ffffffffffffffffffffffffffffffffffffffffffffff')
            file = request.session['grafik']
            file_name = default_storage.save(file.name, file)
            # file = default_storage.open(file_name)
            result_file = self.make_result(file_name)

            print(default_storage)
            request.session['file_result'] = result_file
            return super(TestView, self).get(request, *args, **kwargs)
        else:
            raise Http404




def file_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        # print('sdfsfsfsfsfswfasf')
        # print(my_file.name)
        # with open()
        # file_name = default_storage.save(file.name, file)
        # print(default_storage)
        request.session['grafik'] = file
        # return HttpResponseRedirect(reverse('web_report_card:test'))
    return HttpResponse('file_upload - Done!')

class FileDownloadView(View):
    # Set FILE_STORAGE_PATH value in settings.py
    # folder_path = settings.FILE_STORAGE_PATH
    # Here set the name of the file with extension
    file_name = ''
    # Set the content type value
    content_type_value = 'text/plain'
    content_type_value_xlsx = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def get(self, request, *args, **kwargs):
        # self.file_name = file_name
        # file_path = os.path.join(self.folder_path, self.file_name)
        # file = request.session['grafik']
        # file_name = file.name
        if 'file_result' in request.session:
            file_path = request.session['file_result']
            file = default_storage.open(file_path)
            print(file.name + 'ddddddddd')
            with file as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value_xlsx
                )
                response['Content-Disposition'] = 'attachment; filename=' + file.name
            del request.session['file_result']
            return response
        else:
            raise Http404