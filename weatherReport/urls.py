from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.WeatherView.as_view(), name='index'),
]