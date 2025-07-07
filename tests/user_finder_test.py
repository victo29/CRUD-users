from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.user_repository import UsersRepositorySpy

def test_find():
    first_name = 'meunome'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes['first_name'] == first_name

    assert response ['type'] == 'Users'
    assert response ['count'] == len(response['attributes'])
    assert response ['attributes'] != []
