from abc import ABC, abstractmethod

from src.domain.returns.user_use_cases_retuns import UserDeleteReturn

class UserDelete(ABC):

    @abstractmethod
    def delete(self, id:int) -> UserDeleteReturn:
        raise NotImplementedError("'delete_user' must be implemented")
