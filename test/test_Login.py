from pages.loginpage import LoginPage
from pages.HomePage import HomePage
import pytest
# Launch and Login to an app
@pytest.mark.usefixtures("pre_and_post_action")
class TestLogin:
    def test_actilogin(self):
        driver=self.driver
        lp = LoginPage(driver)
        lp.acti_login()

    def test_actilogout(self):
        driver = self.driver
        hp=HomePage(driver)
        hp.acti_logout()


