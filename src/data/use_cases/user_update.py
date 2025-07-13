from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_update import UserUpdate as UserUpdateInterface
from src.domain.returns.user_use_cases_retuns import UserUpdateReturn
from src.domain.models.users import Users

class UserUpdate(UserUpdateInterface):

    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def update(self, id:int, first_name:str, last_name:str, age:int) -> UserUpdateReturn:
        user = self.__update_user(id, first_name, last_name, age)

        response =  self.__format_response(user)

        return response


    def __update_user(self, id:int, first_name:str, last_name:str, age:int) -> Users:
        user = self.__users_repository.update_user(id, first_name, last_name, age)
        if not user: raise Exception(f'User with id {id} not found')
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
