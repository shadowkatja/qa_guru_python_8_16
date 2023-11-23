"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have
from selene.support.shared import browser, config


@pytest.fixture()
def windows_size_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def windows_size_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 640

def test_github_desktop(windows_size_desktop):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(windows_size_mobile):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
