import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30

def wait_for_element(browser, locator):
    WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located(locator))


def wait_for_text_to_be_present_in_element(browser, locator, expected_text):
    WebDriverWait(browser, TIMEOUT).until(EC.text_to_be_present_in_element(locator, expected_text))


def wait_for_url_contains(browser, url_part):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.url_contains(url_part))


def wait_for_url_to_be(browser, url):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.url_to_be(url))


def wait_for_invisibility_of_element(browser, element):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.invisibility_of_element(element))


def wait_for_visibility_of_element(browser, locator):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.visibility_of_element_located(locator))


def wait_for_element_to_be_clickable(browser, locator):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.element_to_be_clickable(locator))


def wait_for_staleness(browser, element):
    WebDriverWait(browser, TIMEOUT, TimeoutException).until(EC.staleness_of(element))


def wait_for_condition(condition, timeout=30, interval=0.5):
    start = time.time()
    while not condition and time.time() - start < timeout:
        print(condition)
        time.sleep(interval)
