
import pytest
import time



@pytest.fixture()
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


def test_first(browser):
    time.sleep(1)


def test_second(browser):
    time.sleep(5)
