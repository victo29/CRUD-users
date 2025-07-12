from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_list import UserList as UserListInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserListController(ControllerInterface):
    def __init__(self, use_case: UserListInterface):
        self. __use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__use_case.list_users()
        return HttpResponse(
            status_code=200,
            body={"data": response.model_dump()}
        )
