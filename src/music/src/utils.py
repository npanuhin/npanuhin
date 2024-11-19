import re

from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


REGEX_PROBLEMSET_PROBLEM = \
    r"(?:https:[\\\/]+)?codeforces\.com[\\\/]+problemset[\\\/]+problem[\\\/]+(\d+)[\\\/]+([\w\.\,]+)"


def wait_reload(driver):
    WebDriverWait(driver, 30).until_not(
        EC.presence_of_element_located((By.XPATH, "//div[@id='cf_dummy_element']"))
    )


class HandleReload:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        wait_reload(self.driver)


def prettify_code(code: str) -> str:
    return code.replace('\xa0', '')


def problem_url_components(url: str) -> tuple:
    contest_id, task_name = re.search(REGEX_PROBLEMSET_PROBLEM, url).groups()
    contest_id = int(contest_id)
    return contest_id, task_name
