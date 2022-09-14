from django.urls import path
from . import views

app_name = 'web_report_card'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.MyListView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('test2/', views.TestView2.as_view(), name='test2'),
    path('test-dropzone/', views.TestViewDropzone.as_view(), name='test-dropzone'),
    path('upload/', views.file_upload),
]
