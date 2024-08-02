from selenium import webdriver
import pytest


driver = None
def pytest_addoption(parser):

    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--Url", action = "store", default = "stage")

@pytest.fixture(scope= "class")
def setup(request):

    global driver
    BrowserName = request.config.getoption("--browser_name")
    if BrowserName == "chrome":
        driver = webdriver.Chrome()

    elif BrowserName == "firefox":
        driver = webdriver.Firefox()
    elif BrowserName == "IE":
        driver = webdriver.Edge()
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://legacy.r-e-solved.com/Warehouse2/")
    driver.implicitly_wait(5)
    yield
    driver.close()

@pytest.fixture(scope= "class")
def Resolved_setup(request):
    global driver
    BrowserName = request.config.getoption("--browser_name")
    if BrowserName == "chrome":
        driver = webdriver.Chrome()
    elif BrowserName == "firefox":
        driver = webdriver.Firefox
    elif BrowserName == "IE":
        driver = webdriver.Ie
    driver.maximize_window()
    request.cls.driver = driver
    driver.get("https://www.r-e-solved.com/")
    driver.implicitly_wait(5)
    yield
    driver.close()
