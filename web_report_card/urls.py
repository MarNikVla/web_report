from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'web_report_card'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('test-dropzone/', views.TestViewDropzone.as_view(), name='test-dropzone'),
    path('upload/', views.file_upload),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]