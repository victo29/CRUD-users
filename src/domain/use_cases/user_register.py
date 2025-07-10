from abc import ABC, abstractmethod

from src.domain.returns.user_use_cases_retuns import UserRegisterReturn

class UserRegister(ABC):

    @abstractmethod
    def register(self, first_name:str, last_name: str, age: int) -> UserRegisterReturn:
        raise NotImplementedError ("'register' must be implemented")
