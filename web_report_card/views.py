from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin, FormView

from web_report_card.forms import DocumentForm, DocumentFormDrop
from web_report_card.models import Document


class HomeView(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/main.html'

    def get_success_url(self):
        return reverse('web_report_card:home')



class TestView(TemplateView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test.html'
    success_url = reverse_lazy('web_report_card:home')

    def get(self, request, *args, **kwargs):
        print('grafik' in request.session)
        if 'grafik' in request.session:
            print('ffffffffffffffffffffffffffffffffffffffffffffff')
            file = request.session['grafik']
            print(file.name)
            return super(TestView, self).get(request, *args, **kwargs)
        else:
            raise Http404




def file_upload(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        print('sdfsfsfsfsfswfasf')
        print(my_file.name)

        request.session['grafik'] = my_file
        # return HttpResponseRedirect(reverse('web_report_card:test'))
    return JsonResponse({'post': 'Done!'})

class FileDownloadView(View):
    # Set FILE_STORAGE_PATH value in settings.py
    # folder_path = settings.FILE_STORAGE_PATH
    # Here set the name of the file with extension
    file_name = ''
    # Set the content type value
    content_type_value = 'text/plain'

    def get(self, request):
        # self.file_name = file_name
        # file_path = os.path.join(self.folder_path, self.file_name)
        # file = request.session['grafik']
        # file_name = file.name
        if 'grafik' in request.session:
            file = request.session['grafik']
            file_name = file.name
            with file as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value
                )
                response['Content-Disposition'] = 'attachment; filename=' + file_name
            del request.session['grafik']
            return response
        else:
            raise Http404