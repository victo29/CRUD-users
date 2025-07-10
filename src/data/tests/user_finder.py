from src.domain.returns.user_use_cases_retuns import UserFinderReturn

class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, first_name:str) -> UserFinderReturn:
        self.find_attributes['first_name'] = first_name

        return UserFinderReturn(
            type = 'Users',
            count = 1,
            attributes = [
                {"first_name": first_name, "last_name": "something"}
            ]
        )
