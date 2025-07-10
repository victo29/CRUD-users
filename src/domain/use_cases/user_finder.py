from abc import ABC, abstractmethod

from src.domain.returns.user_use_cases_retuns import UserFinderReturn

class UserFinder(ABC):

    @abstractmethod
    def find(self, first_name:str) -> UserFinderReturn:
        raise NotImplementedError ("'find' must be implemented")
