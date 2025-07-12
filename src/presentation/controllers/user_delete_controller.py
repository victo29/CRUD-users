from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_delete import UserDelete as UserDeleteInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserDeleteController(ControllerInterface):
    def __init__(self, use_case: UserDeleteInterface):
        self. __use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.query_params['id']
        response = self.__use_case.delete(id)
        return HttpResponse(
            status_code=200,
            body={"data": response.model_dump()}
        )
