from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin, FormView

from web_report_card.forms import DocumentForm, DocumentFormDrop
from web_report_card.models import Document


class HomeView(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/main.html'

    # success_url = reverse_lazy('web_report_card:test')

    def get_success_url(self):
        return reverse('web_report_card:home')

    def post(self, request, *args, **kwargs):
        print('sdfs')
        my_file = request.FILES.get('file')
        # print(my_file)
        request.session['grafik'] = my_file
        # test_url = reverse_lazy('web_report_card:test')
        # Document.objects.create(docfile=my_file)
        print(request.session['grafik'])

        return redirect(self.get_success_url(), foo=my_file)


class TestView(TemplateView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test.html'
    success_url = reverse_lazy('web_report_card:home')

    def get(self, request, *args, **kwargs):
        print('ffffffffffffffffffffffffffffffffffffffffffffff')
        file = request.session['grafik']
        print(file)
        return super(TestView, self).get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     Document.objects.create(**form.cleaned_data)
    #     return redirect(self.get_success_url())


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
        my_file = request.FILES.get('file')
        print('sdfsfsfsfsfswfasf')
        print(my_file.name)

        request.session['grafik'] = my_file
        # return HttpResponseRedirect(reverse('web_report_card:test'))
    return JsonResponse({'post': 'Done!'})
