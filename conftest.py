import pytest


@pytest.fixture(scope='class')
def pre_and_post_action(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/ankita/PycharmProjects/Automation_POm/drivers/chromedriver.exe")
    driver.get("http://demo.actitime.com")
    driver.implicitly_wait(30)
    request.cls.driver = driver