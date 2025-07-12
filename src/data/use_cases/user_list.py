from typing import List

from src.domain.use_cases.user_list import UserList as UserListInterface
from src.domain.returns.user_use_cases_retuns import UserListReturn
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UserList(UserListInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self. __users_repository = users_repository

    def list_users(self) -> UserListReturn:
        users = self.__get_users()
        response = self.__format_response(users)

        return response

    def __get_users(self) -> List[Users]:
        users = self.__users_repository.list_users()
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> UserListReturn:
        attributes = []
        for user in users:
            attributes.append({"id":user.id ,"first_name": user.first_name, "age": user.age})

        return UserListReturn(
            type = 'Users',
            count = len(users),
            attributes = attributes
        )
