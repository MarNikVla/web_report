from django.urls import path
from . import views

app_name = 'web_report_card'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.MyListView.as_view(), name='home'),
    path('test', views.TestView.as_view(), name='test'),
]
