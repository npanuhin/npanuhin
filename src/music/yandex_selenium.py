# from collections import defaultdict
# from contextlib import suppress
from traceback import print_exc
from time import sleep
# import os

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.common.exceptions import JavascriptException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from fake_useragent import UserAgent
from selenium import webdriver
import jstyleson as json

# from seleniumbase import Driver


CONFIG_PATH = 'config.json'


with open("src/scripts/wait.js", 'r', encoding="utf-8") as file:
    DEFAULT_SCRIPT = file.read()
# with open("src/scripts/create_dummy_element.js", 'r', encoding="utf-8") as file:
#     DEFAULT_SCRIPT += file.read()


def execute_script(driver, path: str, *arguments, run_async: bool = False):
    with open(path, 'r', encoding="utf-8") as file:
        script = DEFAULT_SCRIPT + file.read().strip()

    if run_async:
        return driver.execute_async_script(script, *arguments)
    return driver.execute_script(script, *arguments)


def main():
    print('Starting web browser...')
    with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
        config = json.load(file)

    try:
        service = Service(log_path='geckodriver.log')
        options = webdriver.FirefoxOptions()

        # ua = UserAgent()
        # user_agent = ua.random
        # print(user_agent)
        # options.add_argument(f'user-agent={user_agent}')
        options.add_argument(
            f'user-agent=User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
        )

        if config['headless']:
            options.add_argument('--headless')

        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference('devtools.selfxss.count', 100)
        options.profile = firefox_profile

        driver = webdriver.Firefox(service=service, options=options)
        # driver = Driver(uc=True, headless=config['headless'])
    except Exception:
        # print(e)
        print_exc()

    # ================================================== Authorizing ===================================================
    print('Authorizing...')

    while True:
        try:
            driver.get('https://passport.yandex.ru/auth')
            break
        except Exception:
            print('Error while opening the page, retrying...')
            sleep(0.1)

    # execute_script(driver, 'src/scripts/login.js', config['username'], config['password'])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#passp-field-login'))
    ).send_keys(config['username'])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#passp\\:sign-in'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#passp-field-passwd'))
    ).send_keys(config['password'])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#passp\\:sign-in'))
    ).click()

    print('Logged in')

    input()


if __name__ == '__main__':
    main()
