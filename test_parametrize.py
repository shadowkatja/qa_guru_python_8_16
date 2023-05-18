from dataclasses import dataclass

import pytest


def test_with_param(browser):
    pass

def test_with_matrix_param(browser, test_user):
    pass


def test_with_param_marks(browser):
    pass

# ---------------------------------------------


def browser(request):
    if request.param == "Chrome":
        return
    if request.param == "Firefox":
        return
    if request.param == "Safari":
        return


def test_with_parametrized_fixture(browser):
    pass


def test_with_indirect_parametrization(browser):
    pass


chrome_only = None


def test_chrome_extension(browser):
    pass


@dataclass
class User:
    id: int
    name: str
    age: int
    description: str


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


@pytest.mark.parametrize("user", [user1, user2])
def test_users(user):
    pass
