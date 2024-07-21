from fastapi import APIRouter, Depends,  Form, Request
from fastapi.responses import FileResponse
from app.database.cruds import ApplicationCRUD
from app.service.weather_service.weather import WeatherSearch
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
staticfiles = StaticFiles(directory="app")
router.mount("/static", staticfiles, name="static")

wearher_search = WeatherSearch()
app_crud = ApplicationCRUD()


@router.get("/", response_class=FileResponse)
async def index():

    return FileResponse("app/templates/index.html")



@router.post("/weather")
async def get_weather(request:Request, location=Form()):
    app_crud.add_record(request=location)
    
    wearher = wearher_search.get_weather(location)

    date = datetime.now(timezone.utc)
    return templates.TemplateResponse("weather.html", {"request": request, 
                                                       "weather_now": wearher.get("hourly"),
                                                       "daily": wearher.get("daily"), 
                                                       "date": f"{date.hour}:{date.minute}"})