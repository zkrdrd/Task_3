from pathlib import Path

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from helpers.data import URL
from helpers.helpers import generate_random_string, generate_unique_email


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser")
    driver.get(URL.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    response = requests.post(
        f"{URL.MAIN_PAGE_URL}/api/auth/register",
        json={
            "email": generate_unique_email(),
            "password": generate_random_string(),
            "name": generate_random_string(),
        },
        timeout=10,
    ).json()
    yield [response["user"]["email"], response["user"]["password"]]
    if requests.delete(
        f"{URL.MAIN_PAGE_URL}/api/auth/user",
        timeout=10,
    ).status_code():
        return False
