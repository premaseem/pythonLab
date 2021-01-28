from typing import Optional

from fastapi import FastAPI, status, Form,UploadFile, File
from typing import List
from pydantic import BaseModel
from starlette.responses import JSONResponse
from fastapi.responses import HTMLResponse
from weather_service import WeatherService

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...)):
    return {"username": username}

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

class WeatherRequestModel(BaseModel):
    lat: float
    lon: float
    unit: Optional[str] = "F"

class WeatherResponseModel(BaseModel):
    currentTemp: float
    highTemp: float
    lowTemp: float
    unit : str




@app.post("/weather", response_model=WeatherResponseModel, status_code=status.HTTP_200_OK)
async def create_item(item: WeatherRequestModel, serviceId: Optional[int] = 1):

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



