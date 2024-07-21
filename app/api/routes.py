from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse, FileResponse
from app.database.cruds import ApplicationCRUD
from app.database.database import Database
from app.api.models import UserRequest
from app.service.weather_service.weather import WeatherSearch
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.utils.message_render import message_render


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
staticfiles = StaticFiles(directory="app")
router.mount("/static", staticfiles, name="static")

wearher_search = WeatherSearch()
app_crud = ApplicationCRUD()


@router.get("/")
async def index():

    return FileResponse("app/templates/index.html")



@router.post("/weather")
async def get_weather(location: UserRequest):

    app_crud.add_record(request=location.sity)
    
    wearher = wearher_search.get_weather(location.sity)

    messege = message_render(data=wearher, location=location.sity)
    return {"message": f"{messege}"}