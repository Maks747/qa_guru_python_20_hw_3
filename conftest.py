import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser.config.window_width = 1351 # задает ширину окна браузера
    browser.config.window_height = 607  # задает высоту окна браузера
    yield
    browser.quit()  # закрывает браузер после выполнения теста
