import pytest
import sys

from src.pages.NaukriHomePage import NaukriHome

sys.path.append("../../")
from utilities.baseclass import baseClass
from src.pages.NaukriLoginPage import NaukriLogin

class TestGoogleHome(baseClass):

  def test_pytest_open_google(self):
    self.driver.get("https://www.google.com/")
    naukri = NaukriLogin(self.driver)
    naukri.enter_text_in_google_search("naukri")
    naukri.login_naukri("dixit.vuppuluri30@gmail.com","191642")
    url = self.driver.current_url
    assert "homepage" in url
    naukrihome = NaukriHome(self.driver)
    naukrihome.selectEditProfile()

  #def test_pytest_update_naukri(self):
    #naukrihome = NaukriHome(self.driver)
    #naukrihome.selectEditProfile()







