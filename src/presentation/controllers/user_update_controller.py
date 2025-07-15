
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_update import UserUpdate as UserUpdateInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserUpdateController(ControllerInterface):

    def __init__(self, use_case: UserUpdateInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.query_params
        first_name = http_request.body['first_name']
        last_name = http_request.body['last_name']
        age = http_request.body['age']

        response = self.__use_case.update(id, first_name, last_name, age)

        return HttpResponse(
            status_code=200,
            body={"data": response.model_dump()}
        )
