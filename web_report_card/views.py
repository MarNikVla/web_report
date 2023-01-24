import pathlib

from django.core.files.storage import default_storage
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import escape_uri_path

from django.views import View
from django.views.generic import TemplateView

from web_report_card.main import make_table_file_for_web_app, make_grafik_file_for_web_app
from web_report_card.tasks import del_file_task

IN_SESSION_FILE_KEY = 'uploaded_file'
FILE_PATH = 'File_path'


class HomeView(TemplateView):
    template_name = 'web_report_card/table.html'


class GrafikView(TemplateView):
    template_name = 'web_report_card/grafik.html'


class NotCorrectFileUploadView(TemplateView):
    template_name = 'web_report_card/errors.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['error'] = kwargs['error']
        # data['task'] = create_task
        return data


class ResultTableView(TemplateView):
    template_name = 'web_report_card/result.html'

    def make_result(self, file_name):
        result_file_path = make_table_file_for_web_app(file_name)
        return result_file_path

    def get(self, request, *args, **kwargs):
        if IN_SESSION_FILE_KEY in request.session:
            file = request.session[IN_SESSION_FILE_KEY]
            file_path = default_storage.save(file.name, file)
            del_file_task.apply_async((file_path,), countdown=60 * 1)
            del request.session[IN_SESSION_FILE_KEY]
            try:
                result_file_path = self.make_result(file_path)
                request.session[FILE_PATH] = result_file_path
            except Exception as e:
                return HttpResponseRedirect(
                    reverse('web_report_card:not_correct_file_upload', kwargs={'error': e}))
            return super(ResultTableView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(
                reverse('web_report_card:not_correct_file_upload',
                        kwargs={'error': 'Файл не загружен'}))


class ResultGrafikView(TemplateView):
    template_name = 'web_report_card/result.html'

    def make_result(self, file_name):
        result_file_path = make_grafik_file_for_web_app(file_name)
        return result_file_path

    def get(self, request, *args, **kwargs):
        if IN_SESSION_FILE_KEY in request.session:
            file = request.session[IN_SESSION_FILE_KEY]
            file_path = default_storage.save(file.name, file)
            del_file_task.apply_async((file_path,), countdown=60 * 1)
            del request.session[IN_SESSION_FILE_KEY]
            try:
                result_file_path = self.make_result(file_path)
                request.session[FILE_PATH] = result_file_path
            except Exception as e:
                return HttpResponseRedirect(
                    reverse('web_report_card:not_correct_file_upload', kwargs={'error': e}))
            return super(ResultGrafikView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(
                reverse('web_report_card:not_correct_file_upload',
                        kwargs={'error': 'Файл не загружен'}))


def file_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        request.session[IN_SESSION_FILE_KEY] = file

    return HttpResponse('Done!')


class FileDownloadView(View):
    content_type_value_xlsx = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def get(self, request, *args, **kwargs):
        if FILE_PATH in request.session:
            file_path = request.session[FILE_PATH]
            file = default_storage.open(file_path)
            result_file_path_obj = pathlib.Path(file.name)
            with file as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value_xlsx
                )
                # response[
                #     'Content-Disposition'] = 'attachment; filename=' + result_file_path_obj.name
                response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(
                    result_file_path_obj.name)
            del request.session[FILE_PATH]
            default_storage.delete(file_path)
            return response
        else:
            raise Http404
