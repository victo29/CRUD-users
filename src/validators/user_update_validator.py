from cerberus import Validator
from fastapi import Request

from src.errors.types import HttpUnprocessableEntityError

async def user_update_validator(request: Request):

    body_validator = Validator({
        "first_name": { "type": "string", "required": True, "empty": False },
        "last_name": { "type": "string", "required": True, "empty": False },
        "age": { "type": "integer", "required": True, "empty": False }
    }, require_all=True)

    query_validator = Validator({
        "id": { "type": "integer", "required": True, "empty": False },
    }, require_all=True)

    body = await request.json()
    query = dict(request.query_params)

    converted_query = {
        "id": int(query["id"]) if "id" in query and query["id"].isdigit() else query.get("id")
    }

    response_body = body_validator.validate(body)
    response_query = query_validator.validate(converted_query)

    errors = {}

    if not response_body:
        errors['body'] = body_validator.errors
    if not response_query:
        errors['query'] = query_validator.errors

    if errors:
        raise HttpUnprocessableEntityError(errors)
