from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.domain.models.users_input import Users

from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_list_composer import user_list_composer
from src.main.composers.user_delete_composer import user_delete_composer
from src.main.composers.user_update_composer import user_update_composer

from src.presentation.http_types.http_request import HttpRequest

from src.errors.error_handler import handle_erros

router = APIRouter(
    prefix="/users",
    tags=["collect"],
    responses={404: {"description": "Not found"}},
)

@router.get('/find')
def find_user(first_name:str):
    http_request = HttpRequest(query_params=first_name)

    try:
        controller = user_finder_composer()
        http_response = controller(http_request)

    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code=http_response.status_code, content=http_response.body)

@router.post('/register')
def register_user(user: Users):
    http_request = HttpRequest(body=user.model_dump())
    try:
        controller =  user_register_composer()
        http_response = controller(http_request)

    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code=http_response.status_code, content=http_response.body)


@router.get('/listUsers')
def list_users():
    http_request = HttpRequest()
    try:
        controller = user_list_composer()
        http_response = controller(http_request)

    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.delete('/delete')
def delete_user(id:int):
    http_request = HttpRequest(query_params=id)
    try:
        controller = user_delete_composer()
        http_response = controller(http_request)

    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)

@router.put('/update')
def update_user(id:int, user: Users):
    http_request = HttpRequest(query_params=id,body=user.model_dump())
    try:
        controller = user_update_composer()
        http_response = controller(http_request)
    except Exception as exception:
        http_response = handle_erros(exception)

    return JSONResponse(status_code= http_response.status_code, content= http_response.body)
