from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import FileResponse
from app.database.cruds import ApplicationCRUD
from app.service.weather_service.weather import WeatherSearch
from fastapi import Cookie, Depends, Response
from app.api.models import UserRequest
from fastapi.templating import Jinja2Templates
from app.errors.service_errors import InvalidLocation



router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/cookie")
async def cookie(response: Response,
           crud: ApplicationCRUD = Depends(ApplicationCRUD)):
    user_id = crud.add_user()
    response.set_cookie(key="user_id", value=user_id)
    return  {"message": "куки установлены"}



@router.get("/")
async def index(request: Request):

    return  templates.TemplateResponse(request, "index.html")



@router.post("/weather")
async def get_weather(location:UserRequest, 
                      user_id: str | None = Cookie(default=None),
                      crud: ApplicationCRUD = Depends(ApplicationCRUD),
                      weather_search: WeatherSearch = Depends(WeatherSearch)):
    
    crud.add_record(request=location.sity, user_id=user_id)

    try:
        weather = weather_search.get_weather(location.sity)
    except InvalidLocation:
        raise HTTPException(status_code=404, detail="Location not found")

    return {"message": weather}