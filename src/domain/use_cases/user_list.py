from abc import ABC, abstractmethod

from src.domain.returns.user_use_cases_retuns import UserListReturn

class UserList(ABC):

    @abstractmethod
    def list_users(self) -> UserListReturn:
        raise NotImplementedError("'list_users' must be implemented")
