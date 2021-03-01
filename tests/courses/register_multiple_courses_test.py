from pages.courses.register_courses_pages import RegisterCoursesPages
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rcp = RegisterCoursesPages(self.driver)
        self.ts = TestStatus(self.driver)

    @data(("JavaScript for beginners", "5500000000000004", "01/28", "111"), ("Learn Python 3 from scratch", "5500000000000004", "05/25", "465"))
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
        self.driver.find_element_by_link_text("ALL COURSES").click()
