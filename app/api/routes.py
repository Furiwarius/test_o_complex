from fastapi import APIRouter, Depends,  Form
from fastapi.responses import FileResponse
from app.database.cruds import ApplicationCRUD
from app.service.weather_service.weather import WeatherSearch
from fastapi import Cookie, Depends, Response, Body


router = APIRouter()


@router.get("/cookie")
def cookie(response: Response,
           crud: ApplicationCRUD = Depends(ApplicationCRUD)):
    user_id = crud.add_user()
    response.set_cookie(key="user_id", value=user_id)
    return  {"message": "куки установлены"}



@router.get("/", response_class=FileResponse)
async def index():

    return FileResponse("app/templates/index.html")



@router.post("/weather")
async def get_weather(location = Body(), 
                      user_id: str | None = Cookie(default=None),
                      crud: ApplicationCRUD = Depends(ApplicationCRUD),
                      weather_search: WeatherSearch = Depends(WeatherSearch)):
    
    crud.add_record(request=location['location'], user_id=user_id)
    weather = weather_search.get_weather(location['location'])

    return {"weather": weather}