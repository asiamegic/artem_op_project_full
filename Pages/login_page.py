from selenium.webdriver.common.by import By
from config.config import TestData
from config.locator import Locator
from Pages.BasePage import BasePage
import time


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def do_login(self, username, password):
        self.do_click(Locator.sign_in_button)
        self.do_send_keys(Locator.username, username)
        self.do_send_keys(Locator.password, password)
        self.do_click(Locator.login)
