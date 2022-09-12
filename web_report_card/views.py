from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin, FormView

from web_report_card.forms import DocumentForm, DocumentFormDrop
from web_report_card.models import Document


# class FormListView(FormMixin, ListView):




class MyListView(FormView):
    form_class = DocumentForm
    template_name = 'web_report_card/main.html'
    success_url = reverse_lazy('web_report_card:home')

    def form_valid(self, form):
        Document.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())


class HomeView(TemplateView):
    template_name = 'web_report_card/main.html'

class TestView(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test.html'
    success_url = reverse_lazy('web_report_card:home')

    def form_valid(self, form):
        Document.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())

class TestView2(FormView):
    form_class = DocumentFormDrop
    template_name = 'web_report_card/test2.html'
    success_url = reverse_lazy('web_report_card:home')

    def form_valid(self, form):
        Document.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())