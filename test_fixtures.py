
import pytest

@pytest.fixture
def browser():
    print("Браузер")
    yield
    print("Закрываем браузер")

@pytest.fixture
def login_page(browser): #эта фикстура зависит от фикстуры браузера
    print("Логин пейдж")
    pass

@pytest.fixture
def user():
    print("Юзер")
    return "username", "password"

#указываем в скобках фикстуры, которые должны быть запущены
def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"