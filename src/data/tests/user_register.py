from src.domain.returns.user_use_cases_retuns import UserRegisterReturn

class UserRegistertSpy:
    def __init__(self) -> None:
        self.register_attributes = {}

    def  register(self, first_name:str, last_name:str, age:int) -> UserRegisterReturn:
        return UserRegisterReturn(
            type = 'Users',
            count = 1,
            attributes ={"first_name": first_name, "last_name": last_name, "age": age}
        )
