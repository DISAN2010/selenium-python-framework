from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lg.login("test1@email.com", "test@2010")
        result1 = self.lg.verifyTitle()
        self.ts.mark(result1, "Title is correct")
        result2 = self.lg.verifyLoginSuccessful()
        self.ts.markFinal("test_ValidLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lg.logout()
        self.lg.login("test1@email.com", "abcabc")
        result = self.lg.verifyLoginFailed()
        assert result == True

