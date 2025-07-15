from cerberus import Validator
from fastapi import Request

from src.errors.types import HttpUnprocessableEntityError

async def user_register_validator(request: Request):

    body_validator = Validator({
        "first_name": { "type": "string", "required": True, "empty": False },
        "last_name": { "type": "string", "required": True, "empty": False },
        "age": { "type": "integer", "required": True, "empty": False }
    }, require_all=True)

    body = await request.json()

    response =  body_validator.validate(body)

    if not response:
        raise HttpUnprocessableEntityError(body_validator.errors)
