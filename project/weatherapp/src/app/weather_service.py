import requests

class WeatherService:
    def __init__(self,lat,lon,unit="F",service_code=1):
        self.lat = lat
        self.lon = lon
        self.unit = unit
        self.service = service_code


    def service1(self):
        url = "http://fake-weather.shipwell.com/accuweather?latitude={}&longitude={}".format(self.lat,self.lon)

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200:
            return

        lst = response.json().get("simpleforecast").get("forecastday")
        for day in lst:
            ht = day.get("high")
            lt = day.get("low")
            ct = day.get("current")

        if self.unit == "F":
            ht = ht.get("fahrenheit")
            lt = lt.get("fahrenheit")
            ct = ct.get("fahrenheit")
        else:
            ht = ht.get("celsius")
            lt = lt.get("celsius")
            ct = ct.get("celsius")
        d = {
                "currentTemp": ct,
                "highTemp": ht,
                "lowTemp": lt,
                "unit" : self.unit,
                "extra":123
            }
        return d

    def service2(self):
        url = "http://fake-weather.shipwell.com/weatherdotcom"

        payload= {
            "lat":self.lat,
            "lon":self.lon
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, json=payload)
        if response.status_code != 200:
            return
        return  response.json()

    def get_weather_data(self, s_code=1):
        rsp = None
        if s_code == 1:
            rsp = self.service1()


        if s_code == 2:
            rsp = self.service2()

        return rsp



# o = WeatherService(33.3,44.4)
# print(o.service2())