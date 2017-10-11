from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class WeatherView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        weathers = super(WeatherView, self).get_context_data(**kwargs)
        weathers['weathers'] = self.request.weather_data

        return weathers


# class DinajpurWeather(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         dinajpur = super(DinajpurWeather, self).get_context_data()
#
#         dinajpur['din_weather'] = self.request.dinajpur_weather_data['main']['temp']
#         dinajpur['din_pressure'] = self.request.dinajpur_weather_data['main']['pressure']
#         dinajpur['din_humidity'] = self.request.dinajpur_weather_data['main']['humidity']
#         dinajpur['din_temp_min'] = self.request.dinajpur_weather_data['main']['temp_min']
#         dinajpur['din_temp_max'] = self.request.dinajpur_weather_data['main']['temp_max']
#
#         return dinajpur