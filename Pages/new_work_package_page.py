from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage
from config.locator import Locator
from Pages.project_overview import Project
from Pages.login_page import Login

import time


class New_Work_Package(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_work(self, package_name, package_des):
        self.do_click(Locator.workpackage)
        self.do_click(Locator.menu)
        value11 = self.get_element_text(Locator.value1)
        value22 = self.get_element_text(Locator.value2)
        value = value11 + " " + value22
        assert value == "New TASK"
        self.do_send_keys(Locator.package_name, package_name)
        self.do_send_keys(Locator.package_des, package_des)
        self.do_click(Locator.save_button)
        time.sleep(2)
        rowcount1 = self.do_count_length(Locator.rowcount1)

        value33 = self.get_element_text(Locator.value3)
        assert value33 == "TASK"
        value44 = self.get_element_text(Locator.value4)
        assert value44 == "PYTHON"
