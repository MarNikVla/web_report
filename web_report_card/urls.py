from django.conf import settings
from django.template.defaulttags import url
from django.urls import path, include
from . import views

app_name = 'web_report_card'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('grafik/', views.GrafikView.as_view(), name='grafik'),
    path('table-result/', views.ResultTableView.as_view(), name='result'),
    path('download/', views.FileDownloadView.as_view(), name='download'),
    path('not_correct_file_upload/<str:error>/', views.NotCorrectFileUploadView.as_view(),
         name='not_correct_file_upload'),
    path('upload/', views.file_upload),
]
