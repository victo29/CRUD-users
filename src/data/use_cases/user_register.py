from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.returns.user_use_cases_retuns import UserRegisterReturn

class UserRegister(UserRegisterInterface):

    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self. __user_repository = user_repository

    def register(self, first_name:str, last_name:str, age:int) -> UserRegisterReturn:
        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__registry_user_infromations(first_name, last_name, age)
        response = self.__format_response(first_name,last_name,age)
        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception('Name is invalid to search')

        if len(first_name) > 18:
            raise Exception('Name is too long to search')

    def __registry_user_infromations(self, first_name:str, last_name:str, age:int) -> None:
        self.__user_repository.insert_user(first_name, last_name, age)

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
