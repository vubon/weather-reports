import requests


class WeatherReport(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        dhakaURL = "http://api.openweathermap.org/data/2.5/weather?q=Dhaka&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
        DinjURL = "http://api.openweathermap.org/data/2.5/weather?q=Dinajpur&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
        RajURL = "http://api.openweathermap.org/data/2.5/weather?q=Rajshahi&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
        barisalURL = "http://api.openweathermap.org/data/2.5/weather?q=Barisal&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
        ChittagongURL = "http://api.openweathermap.org/data/2.5/weather?q=Chittagong&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
        KhulnaURL = "http://api.openweathermap.org/data/2.5/weather?q=Khulna&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"

        dinjData = requests.get(DinjURL).json()
        dhakaData = requests.get(dhakaURL).json()
        rajData = requests.get(RajURL).json()
        barisalData = requests.get(barisalURL).json()
        ChittagongData = requests.get(ChittagongURL).json()
        KhulnaData = requests.get(KhulnaURL).json()

        # request.dhaka_weather_data = dhakaData
        #print(dhakaData)
        request.weather_data = [dhakaData,dinjData,rajData,barisalData,ChittagongData,KhulnaData]

        response = self.get_response(request)

        return response


# class DinajpurWeather(object):
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         DinjURL = "http://api.openweathermap.org/data/2.5/weather?q=Dinajpur&units=metric&APPID=4f943161a5defb2123bb8b4bcc561bb8"
#
#         dinjData = requests.get(DinjURL).json()
#         request.dinajpur_weather_data = dinjData
#
#         response = self.get_response(request)
#
#         return response
