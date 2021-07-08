from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage
from config.locator import Locator
from Pages.login_page import Login

import time


class NewProject(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def do_new_project(self, project_name1):
        self.do_send_keys(Locator.project_name, project_name1)
        self.get_attribute(Locator.project_name)
        name1 = project_name1.replace(' ', '-').lower()
        for char in name1:
            if char in "?.!:;/'@#$%^*()?/":
                name1 = name1.replace(char, '-')
        self.do_clear(Locator.project_name)
        self.do_send_keys(Locator.project_name, name1)
        self.do_click(Locator.advanced_setting)
        validation = self.get_element_text(Locator.advance_validation)
        assert validation == "Description"
        self.do_send_keys(Locator.description, "this is  Python Project")
        self.do_click(Locator.status_button)
        self.do_click(Locator.on_track)
        self.do_click(Locator.save)
        time.sleep(2)
