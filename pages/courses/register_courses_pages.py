from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class RegisterCoursesPages(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_box = "//input[@class='form-control find-input dynamic-text']"
    _searchButton = "//button[@class='find-course search-course']"
    _course = "//h4[contains(text(),'{0}')]"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cardNumber = "cardnumber"
    _expiryDate = "exp-date"
    _cvc = "cvc"
    _submit = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg " \
              "btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//div[@class='alert alert-danger']"

    def enterCourse(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementCLick(self._searchButton, locatorType="xpath")

    def clickCourse(self, course):
        self.elementCLick(locator=self._course.format(course), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementCLick(self._enroll_button, locatorType="xpath")

    def enterCardNumber(self, cardNumber):
        cardSearchBox = "//iframe[@title='Secure card number input frame']"
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(cardSearchBox))
        self.sendKeys(cardNumber, self._cardNumber, locatorType="name")
        self.driver.switch_to.default_content()

    def enterExpiryDate(self, expiryDate):
        expiryDateSearchBox = "//iframe[@title='Secure expiration date input frame']"
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(expiryDateSearchBox))
        self.sendKeys(expiryDate, self._expiryDate, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCvc(self, cvc):
        cvcSearchBox = "//iframe[@title='Secure CVC input frame']"
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(cvcSearchBox))
        self.sendKeys(cvc, self._cvc, locatorType="name")
        self.driver.switch_to.default_content()

    def clickSubmit(self):
        self.elementCLick(self._submit, locatorType="xpath")

    def enterPaymentDetails(self, cardNumber, expiryDate, cvc):
        self.enterCardNumber(cardNumber)
        self.enterExpiryDate(expiryDate)
        self.enterCvc(cvc)

    def enrollCourse(self, cardNumber="", expiryDate="", cvc=""):
        self.clickEnrollButton()
        self.webScroll(direction="down")
        self.enterPaymentDetails(cardNumber, expiryDate, cvc)
        self.clickSubmit()

    def verifyEnrollFailed(self):
        result = self.isElementDisplayed(self._enroll_error_message, locatorType="xpath")
        return result
