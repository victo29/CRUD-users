from typing import Dict, List

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.domain.returns.user_use_cases_retuns import UserFinderReturn
from src.domain.models.users import Users


class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None :
        self.__users_repository =  users_repository

    def find(self, first_name:str) -> UserFinderReturn:
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        response = self.__format_response(users)
        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception('Name is invalid to search')

        if len(first_name) > 18:
            raise Exception('Name is too long to search')

    def __search_user(self, first_name:str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if not users: raise Exception('User not found')
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> UserFinderReturn:
        attributes = []
        for user in users:
            attributes.append({"first_name": user.first_name, "age": user.age})

        return UserFinderReturn(
            type = 'Users',
            count = len(users),
            attributes = attributes
        )
