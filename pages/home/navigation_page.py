from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _my_courses = "MY COURSES"
    _user_icon = "//button[@id='dropdownMenu1']/img"

    def navigateToHome(self):
        self.elementCLick(self._home, locatorType="link")

    def navigateToAllCourses(self):
        self.elementCLick(self._all_courses, locatorType="link")

    def navigateToSupport(self):
        self.elementCLick(self._support, locatorType="link")

    def navigateToMyCourses(self):
        self.elementCLick(self._my_courses, locatorType="link")

    def navigateToUserIcon(self):
        self.elementCLick(self._user_icon, locatorType="xpath")
