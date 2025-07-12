from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_list_composer import user_list_composer
from src.main.composers.user_delete_composer import user_delete_composer

router = APIRouter(
    prefix="/users",
    tags=["collect"],
    responses={404: {"description": "Not found"}},
)

@router.get('/find')
async def find_user(request: Request):
    controller = user_finder_composer()
    http_response = await request_adapter(request,controller)

    return JSONResponse(status_code=http_response.status_code, content=http_response.body)

@router.post('/register')
async def register_user(request: Request):
    controller = user_register_composer()
    http_response = await request_adapter(request,controller)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.get('/listUsers')
async def list_users(request: Request):
    controller = user_list_composer()
    http_response = await request_adapter(request,controller)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.delete('/delete')
async def delete_user(request: Request):
    controller = user_delete_composer()

    http_response = await request_adapter(request,controller)
    return JSONResponse(status_code= http_response.status_code, content= http_response.body)
