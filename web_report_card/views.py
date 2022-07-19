from django.http import Http404
from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin

from web_report_card.forms import DocumentForm
from web_report_card.models import Document


# class FormListView(FormMixin, ListView):




class MyListView(ListView):

    model = Document
    template_name = 'web_report_card/main.html'

    def get(self, request, *args, **kwargs):
        form = DocumentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = DocumentForm(request.POST)


class HomeView(TemplateView):
    template_name = 'web_report_card/main.html'
