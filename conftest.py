import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_width = 1366
    browser.config.window_height = 607
    yield
    browser.quit()
