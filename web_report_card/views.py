from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin, FormView

from web_report_card.forms import DocumentForm, DocumentFormDrop
from web_report_card.models import Document


class HomeView(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/main.html'
    success_url = reverse_lazy('web_report_card:test')


    def post(self, request, *args, **kwargs):
        print('sdfs')
        my_file = request.FILES.get('file')
        # print(my_file)
        # print(self)
        request.session['grafik'] = my_file
        # test_url = reverse_lazy('web_report_card:test')
        # redirect(test_url)
        # Document.objects.create(docfile=my_file)
        # return redirect(test_url)
        print(request.session['grafik'])
        return redirect(self.get_success_url())

class TestView(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test.html'
    success_url = reverse_lazy('web_report_card:home')

    def get(self, request, *args, **kwargs):
        print('ffffffffffffffffffffffffffffffffffffffffffffff')
        file = request.session['grafik']
        print(file)
        return super(TestView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        Document.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())


class TestViewDropzone(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test dropzone.html'
    success_url = reverse_lazy('web_report_card:home')

    def post(self, request, *args, **kwargs):
        print('sdfs')
        my_file = request.FILES.get('file')
        print(my_file)
        # print(self)
        Document.objects.create(docfile=my_file)
        return redirect(self.get_success_url())

    def form_valid(self, form):
        Document.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())


def file_upload(request):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        print(my_file.name)
        Document.objects.create(docfile=my_file)
        # if my_file.name.endswith('.xlsx'):
        #     Document.objects.create(docfile=my_file)
        # else:
        #     return HttpResponse('/ghh')
        return HttpResponse('')
    return JsonResponse({'post':'fasle'})