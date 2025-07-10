from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.user_repository import UsersRepositorySpy

def test_find():
    first_name = 'meunome'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes['first_name'] == first_name

    assert response.type == 'Users'
    assert response.count == len(response.attributes)
    assert response.attributes != []


def test_find_error_in_valid_name():
    first_name = 'meunome12312'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        response = user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Name is invalid to search'


def test_find_error_in_long_name():
    first_name = 'meunomeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        response = user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Name is too long to search'


def test_find_error_user_not_found():

    class UserRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name):
            return []

    first_name = 'nomeInexistente'

    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try:
        response = user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'User not found'
