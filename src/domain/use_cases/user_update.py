from abc import ABC, abstractmethod

from src.domain.returns.user_use_cases_retuns import UserUpdateReturn

class UserUpdate(ABC):

    @abstractmethod
    def update(self, id:int,first_name: str, last_name: str, age: int) -> UserUpdateReturn:
        raise NotImplementedError("'update' must be implemented")
