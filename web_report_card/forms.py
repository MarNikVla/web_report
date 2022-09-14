# -*- coding: utf-8 -*-
from crispy_forms.layout import Submit, Field, Layout, Row, Column
from django import forms
from crispy_forms.helper import FormHelper


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    docfile.widget.attrs.update({'class': 'dropzone container '})


class DocumentFormDrop(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='Drop files here or click to upload'
    )
    docfile.widget.attrs.update({'class': 'dropzone container'})

