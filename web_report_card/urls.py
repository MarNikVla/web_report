from django.conf import settings
from django.template.defaulttags import url
from django.urls import path, include
from . import views


app_name = 'web_report_card'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('download/', views.FileDownloadView.as_view(), name='download'),
    path('upload/', views.file_upload),
]