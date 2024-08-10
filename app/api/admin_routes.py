from fastapi import APIRouter, Depends
from app.database.cruds import ApplicationCRUD
from app.api.models import AdminKey, UserRequest
from app.service.admin_service import AdminService


admin = APIRouter()


@admin.get("/get_count_user")
async def get_count_user(admin_key: AdminKey,
                         crud: ApplicationCRUD = Depends(ApplicationCRUD),
                         admin_service: AdminService = Depends(AdminService)):
    '''
    Получение количества пользователей
    '''

    # Еще не написанные круды для получения данных
    return  {"message": "message"}



@admin.get("/get_count_reauest")
async def get_count_request(admin_key: AdminKey,
                            location: UserRequest,
                            crud: ApplicationCRUD = Depends(ApplicationCRUD),
                            admin_service: AdminService = Depends(AdminService)):
    '''
    Получение количества запросов на данную локацию
    '''

    # Еще не написанные круды для получения данных
    return  {"message": "message"}



@admin.get("/get_max_count_reauest")
async def get_max_count_request(admin_key: AdminKey,
                            crud: ApplicationCRUD = Depends(ApplicationCRUD),
                            admin_service: AdminService = Depends(AdminService)):
    '''
    Получение локации с максимальным 
    количеством запросов
    '''

    # Еще не написанные круды для получения данных
    return  {"message": "message"}