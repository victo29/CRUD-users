from typing import Dict

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None :
        self.__users_repository =  users_repository

    def find(self, first_name:str) -> Dict:

        if not first_name.isalpha():
            raise Exception('Name is invalid to search')

        if len(first_name) > 18:
            raise Exception('Name is too long to search')

        users = self.__users_repository.select_user(first_name)

        if not users:
            raise Exception('User not found')

        response = {
            "type": 'Users',
            "count": len(users),
            "attributes" : users
        }

        return response
