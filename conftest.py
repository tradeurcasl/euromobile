import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose browser language abbrevation")
    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(r"C:\Users\loftyrogue\environments\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


