from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_update import UserUpdate
from src.presentation.controllers.user_update_controller import UserUpdateController

def user_update_composer():
    repository = UsersRepository()
    use_case = UserUpdate(repository)
    controller = UserUpdateController(use_case)

    return controller.handle
