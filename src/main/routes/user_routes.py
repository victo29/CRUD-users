from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_list_composer import user_list_composer
from src.main.composers.user_delete_composer import user_delete_composer
from src.main.composers.user_update_composer import user_update_composer

from src.validators import user_finder_validator, user_register_validator, user_delete_validator, user_update_validator

from src.errors.error_handler import handle_erros

router = APIRouter(
    prefix="/users",
    tags=["collect"],
    responses={404: {"description": "Not found"}},
)

@router.get('/find')
async def find_user(request: Request):
    http_response = None

    try:
        await user_finder_validator(request)
        http_response = await request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code=http_response.status_code, content=http_response.body)

@router.post('/register')
async def register_user(request: Request):
    http_response = None

    try:
        await user_register_validator(request)
        http_response = await request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.get('/listUsers')
async def list_users(request: Request):
    http_response = None

    try:
        http_response = await request_adapter(request, user_list_composer())
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.delete('/delete')
async def delete_user(request: Request):
    http_response = None

    try:
        await user_delete_validator(request)
        http_response = await request_adapter(request, user_delete_composer())
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.put('/update')
async def update_user(request: Request):
    http_response = None

    try:
        await user_update_validator(request)
        http_response = await request_adapter(request, user_update_composer())
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)
