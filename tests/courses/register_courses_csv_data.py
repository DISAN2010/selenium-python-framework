from pages.courses.register_courses_pages import RegisterCoursesPages
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPages(self.driver)
        self.ts = TestStatus(self.driver)
        self.np = NavigationPage(self.driver)

    def setUp(self):
        self.np.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/Jude Disan/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_coursePage(self, courseName, cardNumber, expiryDate, cvc):
        self.rcp.enterCourse(courseName)
        time.sleep(2)
        self.rcp.clickCourse(courseName)
        time.sleep(2)
        self.rcp.enrollCourse(cardNumber, expiryDate, cvc)
        time.sleep(2)
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_EnrollCourse", result, "Payment Failed")
