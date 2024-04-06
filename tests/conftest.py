import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_personal_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1300
    browser.config.window_height = 1000
