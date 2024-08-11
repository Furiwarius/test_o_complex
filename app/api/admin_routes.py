from fastapi import APIRouter, Depends, HTTPException
from app.database.admin_cruds import AdminCRUD
from app.api.models import AdminKey, UserRequest, AdminRequest
from app.service.admin_service import AdminService
from app.errors.service_errors import InvalidKey


admin = APIRouter()


@admin.post("/get_count_user")
async def get_count_user(admin: AdminKey,
                         crud: AdminCRUD = Depends(AdminCRUD),
                         admin_service: AdminService = Depends(AdminService)):
    '''
    Получение количества пользователей
    '''
    try:
        admin_service.key_verification(admin.admin_key)
    except InvalidKey:
        raise HTTPException(status_code=403, detail="Invalid key")
    
    count_user = crud.get_count_user()
    return  {"answer": count_user}



@admin.post("/get_count_reauest")
async def get_count_request(admin_request: AdminRequest,
                            crud: AdminCRUD = Depends(AdminCRUD),
                            admin_service: AdminService = Depends(AdminService)):
    '''
    Получение количества запросов на данную локацию
    '''
    try:
        admin_service.key_verification(admin_request.key.admin_key)
    except InvalidKey:
        raise HTTPException(status_code=403, detail="Invalid key")
    
    count_request = crud.get_count_request(location=admin_request.location.sity)
    return  {"answer": count_request}



@admin.post("/get_max_count_reauest")
async def get_max_count_request(admin: AdminKey,
                            crud: AdminCRUD = Depends(AdminCRUD),
                            admin_service: AdminService = Depends(AdminService)):
    '''
    Получение локации с максимальным 
    количеством запросов
    '''
    try:
        admin_service.key_verification(admin.admin_key)
    except InvalidKey:
        raise HTTPException(status_code=403, detail="Invalid key")

    max_count = crud.get_max_count_request()
    return  {"answer": max_count}