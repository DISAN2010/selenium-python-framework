import utilities.custom_logger as cl
import logging


class Util(object):

    log = cl.customLogger(logging.DEBUG)

    def verifyTextContains(self, actualText, expectedText):
        self.log.info(f"Actual title of Web Application UI is : , {actualText}")
        self.log.info(f"Expected title of Web Application UI is : , {expectedText}")

        if expectedText.lower() in actualText.lower():
            self.log.info("### Verification Successful")
            return True
        else:
            self.log.info("### Verification Failed")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info(f"Actual title of Web Application UI is : , {actualText}")
        self.log.info(f"Expected title of Web Application UI is : , {expectedText}")

        if actualText.lower() == expectedText.lower():
            self.log.info("### Verification Successful")
            return True
        else:
            self.log.info("### Verification Failed")
            return False
