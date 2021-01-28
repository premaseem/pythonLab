## Instruction to run the project 
cd to app file ( ie cd weatherapp/src)
Run command to run fast api server
> uvicorn app:app --reload

### Interactive api docs
http://127.0.0.1:8000/docs


### Test with curl call 

curl -L -X POST 'http://127.0.0.1:8000/weather?serviceId=1' \
-H 'Content-Type: application/json' \
--data-raw '{
"lat":33.3,
"lon":44.4,
"unit":"C"
}'

Sample response in Json
{
"currentTemp": 12.0,
"highTemp": 20.0,
"lowTemp": 10.0,
"unit": "C"
}

### Notes
Get data dynamically in your picked unit F/C
request is validated by model 
response is validated by model 
assign int value to serviceId param to choose different service

### Tests
lookup for tests in test dir

# Shipwell Backend Coding Interview Project Requirements

> Note: We do not require the project to be completed in a specific language or framework. We want you to code in whatever language and framework you feel most comfortable with. The default project is Django, but you are welcome to build it in Flask, Java / Spring Boot, Ruby, or whatever you prefer.

## Goal
Create one REST endpoint  to get the current temperature at a specific latitude/longitude coordinate pair from a 
number of upstream weather services.

### Technical Details

- For this project, we'll use three fake external services, their details are below. Your endpoint should accept an 
argument of which service to use as well as a latitude/longitude coordinate pair. The endpoint should return the
temperature.

### Quickstart
We've provided you with a base Django app to help you get started.

```commandline
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

### Other Languages / Frameworks
[Spring Boot project](https://github.com/shipwell/interview-spring-boot)

#### External Services
##### Accuweather
Endpoint URL Format: `GET` response to `http://fake-weather.shipwell.com/accuweather?latitude=44&longitude=33`

Response Format: 
```json
{
  "simpleforecast": {
    "forecastday": [
      {
        "period": 1,
        "high": {
          "fahrenheit": "68",
          "celsius": "20"
        },
        "low": {
          "fahrenheit": "50",
          "celsius": "10"
        },
        "current": {
          "fahrenheit": "55",
          "celsius": "12"
        },
        "conditions": "Partly Cloudy",
        "icon": "partlycloudy",
        "icon_url": "http://icons-ak.wxug.com/i/c/k/partlycloudy.gif",
        "skyicon": "mostlysunny",
        "pop": 0,
        "qpf_allday": {
          "in": 0.00,
          "mm": 0.0
        }
      }
    ]
  }
}
```

##### NOAA
Endpoint URL Format: `GET` request to `http://fake-weather.shipwell.com/noaa?latlon=44,33`

Response Format: 
```json
{
  "today": {
    "high": {
      "fahrenheit": "68",
      "celsius": "20"
    },
    "low": {
      "fahrenheit": "50",
      "celsius": "10"
    },
    "current": {
      "fahrenheit": "55",
      "celsius": "12"
    }
  }
}
```


##### Weather.com
Endpoint URL Format: `POST` request to `http://fake-weather.shipwell.com/weatherdotcom` with JSON body:
```json
{
  "lat":33.3,
  "lon":44.4
}
```

Response Format: 
```json
{
  "query": {
    "count": 1,
    "created": "2017-09-21T17:00:22Z",
    "lang": "en-US",
    "results": {
      "channel": {
        "units": {
          "temperature": "F"
        },
        "description": "Current Weather",
        "language": "en-us",
        "lastBuildDate": "Thu, 21 Sep 2017 09:00 AM AKDT",
        "ttl": "60",
        "condition": {
          "code": "33",
          "date": "Thu, 21 Sep 2017 08:00 AM AKDT",
          "temp": "37",
          "text": "Mostly Clear"
        },
        "atmosphere": {
          "humidity": "80",
          "pressure": "1014.0",
          "rising": "0",
          "visibility": "16.1"
        },
        "astronomy": {
          "sunrise": "8:42 am",
          "sunset": "9:6 pm"
        },
        "item": {
          "title": "Conditions for Nome, AK, US at 08:00 AM AKDT",
          "lat": "64.499474",
          "long": "-165.405792",
          "pubDate": "Thu, 21 Sep 2017 08:00 AM AKDT",
          "guid": {
            "isPermaLink": "false"
          }
        }
      }
    }
  }
}
```

## Important Considerations
- Endpoint path and request and response format are up to you, however they should adhere to best practices for REST 
API's.
- Although we're only asking for a single endpoint here, please write production level code with the assumption that 
this is just the first part of a much larger integration with these weather partners.

## F.A.Q.
- **Is any there any guarantees on incoming data (such as lat/long's being valid)?** No. This is intended to be
deployed on the internet therefore no data from the client can be guaranteed.


## Stretch Goals
While we expect the above to take the entire time, if you get done early you can work on the following stretch goals:
- Allow the user to request from multiple weather providers and return the average temperature
- Allow the user to specify which temperature unit they want the returned temperature in.
