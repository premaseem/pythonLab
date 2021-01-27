from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse


class Item(BaseModel):
    lat: float
    lon: float
    unit: Optional[str] = "F"

class RespModel(BaseModel):
    currentTemp: float
    highTemp: float
    lowTemp: float
    unit : str


app = FastAPI()
from weather_service import WeatherService
@app.post("/weather",response_model=RespModel)
async def create_item(item: Item, serviceId: Optional[int] = 1):

    # grab request payload params
    item_dict = item.dict()
    lat_v = item_dict.get("lat")
    lon_v = item_dict.get("lon")
    unit_v = item_dict.get("unit")

    # create the service object
    ws = WeatherService(lat_v,lon_v,unit_v)

    # fetch data based on service of choice
    print("Service id",serviceId)
    response = ws.get_weather_data(s_code=serviceId)

    # if response is not recieved from upstream service, return 400 with user friendly message
    if not response:
        return JSONResponse(status_code=400, content={"message": "Service not available"})

    return response



