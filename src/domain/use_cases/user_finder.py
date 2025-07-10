from abc import ABC, abstractmethod

from src.domain.returns.user_finder_retun import UserFinderReturn

class UserFinder(ABC):

    @abstractmethod
    def find(self, first_name:str) -> UserFinderReturn:
        raise NotImplementedError ("'find' must be implemented")
