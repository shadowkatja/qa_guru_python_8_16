"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from selene import browser, have
from selene.support.shared import browser


@pytest.fixture(params=[(1280, 960), (360, 640)])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("browser_size", [(1280, 960)], ids=['1280 * 960'], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(360, 640)], ids=['360 * 640'], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
