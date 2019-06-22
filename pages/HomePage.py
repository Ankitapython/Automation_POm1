class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def acti_logout(self):
        self.driver.find_element_by_id("logoutLink").click()