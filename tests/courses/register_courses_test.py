from pages.courses.register_courses_pages import RegisterCoursesPages
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPages(self.driver)
        self.ts = TestStatus(self.driver)

    def test_coursePage(self):
        self.rcp.enterCourse("JavaScript")
        self.rcp.clickCourse("JavaScript for beginners")
        self.rcp.enrollCourse("5500000000000004", "01/28", "111")
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_EnrollCourse", result, "Payment Failed")
