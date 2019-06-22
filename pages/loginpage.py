from testdata.data import *
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def acti_login(self):
        #login
        self.driver.find_element_by_id("username").send_keys(USERNAME)
        self.driver.find_element_by_name("pwd").send_keys(PASSWORD)
        self.driver.find_element_by_xpath("//div[text()='Login ']").click()