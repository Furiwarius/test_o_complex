from fastapi import APIRouter, Depends,  Form
from fastapi.responses import FileResponse
from app.database.cruds import ApplicationCRUD
from app.service.weather_service.weather import WeatherSearch
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Cookie, Depends, Response


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
staticfiles = StaticFiles(directory="app")
router.mount("/static", staticfiles, name="static")



@router.get("/", response_class=FileResponse)
async def index(response: Response, 
                user_id: str | None = Cookie(default=None), 
                crud: ApplicationCRUD = Depends(ApplicationCRUD)):
        
    if user_id == None:
        user_id = crud.add_user()
        response.set_cookie(key="user_id", value=user_id)

    return FileResponse("app/templates/index.html")



@router.post("/weather")
async def get_weather(response: Response, location=Form(), 
                      user_id: str | None = Cookie(default=None),
                      crud: ApplicationCRUD = Depends(ApplicationCRUD),
                      weather_search: WeatherSearch = Depends(WeatherSearch)):
    
    if user_id == None:
        user_id = crud.add_user()
        response.set_cookie(key="user_id", value=user_id)
    
    else:

        crud.add_record(request=location, user_id=user_id)
        weather = weather_search.get_weather(location)

    return {"weather": weather}