from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage
from config.locator import Locator
from Pages.login_page import Login
import time


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_home(self):
        self.do_click(Locator.project_button)

    def do_home1(self, project_name):
        self.do_click(Locator.projectname)
        self.do_send_keys(Locator.search_type, project_name)
        self.do_action(Locator.drop)
        self.do_click(Locator.drop_click)
        self.do_click(Locator.search)
        time.sleep(3)
