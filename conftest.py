import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from env_config import EnvConfig


@pytest.fixture(scope='function')
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-notifications')
    # chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.implicitly_wait(30)

    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def env_config():
    return EnvConfig()
