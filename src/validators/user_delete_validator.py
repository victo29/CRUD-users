from cerberus import Validator
from fastapi import Request

from src.errors.types import HttpUnprocessableEntityError

async def user_delete_validator(request: Request):

    query_validator = Validator({
        "id": { "type": "integer", "required": True, "empty": False },
    }, require_all=True)

    query = dict(request.query_params)

    converted_query = {
        "id": int(query["id"]) if "id" in query and query["id"].isdigit() else query.get("id")
    }

    response = query_validator.validate(converted_query)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
