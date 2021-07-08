from config.config import TestData
from Pages.BasePage import BasePage
from Pages.new_project_page import NewProject
from config.locator import Locator
from Pages.login_page import Login


class Project(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_project_overview(self):
        project_name2 = self.get_attribute(Locator.projectname)
        print("this is " + project_name2)
        assert project_name2 == TestData.name1

    def do_project_overview1(self):
        rowcount = self.do_count_length(Locator.rowcount)
        self.do_click(Locator.workpackage)
        self.do_click(Locator.menu)
