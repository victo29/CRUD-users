from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.returns.user_use_cases_retuns import UserRegisterReturn
from src.errors.types import HttpBadRequestError

class UserRegister(UserRegisterInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self. __users_repository = users_repository

    def register(self, first_name:str, last_name:str, age:int) -> UserRegisterReturn:
        self.__validate_name(first_name)
        self.__validate_name(last_name)
        self.__validate_integer(age)

        self.__registry_user_infromations(first_name, last_name, age)
        response = self.__format_response(first_name,last_name,age)
        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise HttpBadRequestError('Name is invalid to register')

        if len(name) > 18:
            raise HttpBadRequestError('Name is too long to register')

    @classmethod
    def __validate_integer(cls, value: int) -> None:
        try:
            int(value)
        except Exception:
            raise HttpBadRequestError(f'{value} must be an integer value ')

    def __registry_user_infromations(self, first_name:str, last_name:str, age:int) -> None:
        self.__users_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __format_response(cls, first_name:str, last_name:str, age:int) -> UserRegisterReturn:
        return UserRegisterReturn(
            type='Users',
            count=1,
            attributes={
                "first_name":first_name,
                "last_name": last_name,
                'age': age
            }
        )
