from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.tests.user_register import UserRegistertSpy
from src.presentation.http_types.http_response import HttpResponse
class HttRequestMock():
    def __init__(self) -> None:
        self.body = {"first_name": 'myTest',
                     "last_name": 'something',
                     "age":18}

def test_handle():
    http_request_mock = HttRequestMock()
    use_case = UserRegistertSpy()
    user_finder_controller = UserRegisterController(use_case)
    response = user_finder_controller.handle(http_request_mock)

    print()
    print()
    print(response.body)
    print(response.status_code)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
