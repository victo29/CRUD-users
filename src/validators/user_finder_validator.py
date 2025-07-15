from cerberus import Validator
from fastapi import Request

from src.errors.types import HttpUnprocessableEntityError

async def user_finder_validator(request: Request):

    query_validator = Validator({
        "first_name": { "type": "string", "required": True, "empty": False },
    }, require_all=True)

    response = query_validator.validate(request.query_params)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
