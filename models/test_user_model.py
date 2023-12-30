from typing import Type

import pytest
from faker import Faker

from models.user import UserDBMethods, Base, User
from utility.db import test_engine

fake = Faker()


class TestUserModel:
    def setup_method(self, method):
        print(f"\nSet Up Method:\n{method}")
        Base.metadata.create_all(test_engine)
        self.user_methods = UserDBMethods(test_engine)

    def teardown_method(self, method):
        print(f"\nTear Down Method:\n{method}")

        del self.user_methods

    def test_registration(self):
        username = fake.user_name()
        password = fake.password()
        registered_user = self.user_methods.register_user(username, password)
        assert type(registered_user) == User

    def test_get_user(self):
        user = self.user_methods.register_user(
            username=fake.user_name(),
            password=fake.password()
        )
        assert self.user_methods.get_user(user.username) == user

    def test_get_all_users(self):
        all_users = self.user_methods.get_all_users()
        assert isinstance(all_users, type(list(Type[User])))

    def test_update_user(self):
        some_user = self.user_methods.get_all_users()[0]
        some_user.points = fake.random.randint(10, 20)
        some_user.wins = fake.random.randint(1, 4)
        some_user.played_games = fake.random.randint(4, 10)
        updated_user = self.user_methods.update_user(some_user)
        assert updated_user == some_user


if __name__ == '__main__':
    pytest.main()
