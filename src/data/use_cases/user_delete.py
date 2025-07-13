from src.domain.use_cases.user_delete import UserDelete as UserDeleteInterface
from src.domain.returns.user_use_cases_retuns import UserDeleteReturn
from src.domain.models.users import Users
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError

class UserDelete(UserDeleteInterface):

    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def delete(self, id:int) -> UserDeleteReturn:
        self.__validate_integer(id)

        user= self.__delete_user(id)

        response= self.__format_response(user)

        return response

    @classmethod
    def __validate_integer(cls, value: int) -> None:
        try:
            int(value)
        except Exception:
            raise HttpBadRequestError(f'{value} must be an integer value ')

    def __delete_user(self, id:int) -> Users:
        user = self.__users_repository.delete_user(id)
        if not user: raise HttpNotFoundError(f'User with id {id} not found')
        return user

    @classmethod
    def __format_response(cls, user: Users) -> UserDeleteReturn:
        return UserDeleteReturn(
            type='Users',
            count=1,
            attributes={
                "first_name":user.first_name,
                "last_name": user.last_name,
                'age': user.age
            }
        )
