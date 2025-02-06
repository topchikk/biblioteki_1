

import pytest
from selene import browser



@pytest.fixture(scope="session")
def open_browser():
    browser.config.window_height = 720
    browser.config.window_width = 1280
    browser.open('https://duckduckgo.com')

    yield

    browser.quit()
