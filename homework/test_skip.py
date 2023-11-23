"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have
from selene.support.shared import browser

def desktop(width):
    return width >= 1024


@pytest.fixture(params=[(1920, 1080), (1280, 960), (360, 480), (480, 800)],
                ids=['1920 * 1080', '1280 * 960', '360 * 480', '480 * 800'])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_desktop(browser_size):
    if browser.config.window_width < 1024:
        pytest.skip('Test only for desktop')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    if browser.config.window_width >= 1024:
        pytest.skip('Test only for mobile')
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
