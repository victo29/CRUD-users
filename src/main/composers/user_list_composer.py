from src.data.use_cases.user_list import UserList
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.controllers.user_list_controller import UserListController

def user_list_composer():
    repository = UsersRepository()
    use_case = UserList(repository)
    controller = UserListController(use_case)

    return controller.handle
