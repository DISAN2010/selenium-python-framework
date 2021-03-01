from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginTests():

    def test_validLogin(self):
        baseURL = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        signinLink = driver.find_element(By.XPATH, "//*[@id='navbar-inverse-collapse']//a[@href='/login']")
        signinLink.click()

        username = driver.find_element(By.ID, "email")
        username.send_keys("test1@email.com")

        password = driver.find_element(By.ID, "password")
        password.send_keys("test@2010")

        time.sleep(2)

        loginButton = driver.find_element(By.XPATH, "//div[@id='page']//input[@value='Login']")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']/img")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        time.sleep(3)


cc = LoginTests()
cc.test_validLogin()
