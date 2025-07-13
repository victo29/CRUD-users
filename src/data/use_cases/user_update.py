from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_update import UserUpdate as UserUpdateInterface
from src.domain.returns.user_use_cases_retuns import UserUpdateReturn
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError, HttpNotFoundError

class UserUpdate(UserUpdateInterface):

    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def update(self, id:int, first_name:str, last_name:str, age:int) -> UserUpdateReturn:
        self.__validate_name(first_name)
        self.__validate_name(last_name)
        self.__validate_integer(id)
        self.__validate_integer(age)

        user = self.__update_user(id, first_name, last_name, age)
        response =  self.__format_response(user)
        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise HttpBadRequestError('Name is invalid to update')

        if len(name) > 18:
            raise HttpBadRequestError('Name is too long to update')

    @classmethod
    def __validate_integer(cls, value: int) -> None:
        try:
            int(value)
        except Exception:
            raise HttpBadRequestError(f'{value} must be an integer value ')

    def __update_user(self, id:int, first_name:str, last_name:str, age:int) -> Users:
        user = self.__users_repository.update_user(id, first_name, last_name, age)
        if not user: raise HttpNotFoundError(f'User with id {id} not found')
        return user

    @classmethod
    def __format_response(cls, user: Users) -> UserUpdateReturn:
        return UserUpdateReturn(
            type='Users',
            count=1,
            attributes={
                "id": user.id,
                "first_name":user.first_name,
                "last_name": user.last_name,
                'age': user.age
            }
        )
