import pytest
from pytestUi.test_base import BaseTest
from Pages.home_page import HomePage
from Pages.login_page import Login
from Pages.new_project_page import NewProject
from Pages.project_overview import Project
from config.config import TestData
import time

class Test_Automation_Project(BaseTest):
    def test_Ui_CreateProject(self):
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.homepage = HomePage(self.driver)
        self.newProject = NewProject(self.driver)
        self.project_overview = Project(self.driver)
        self.login.do_login(TestData.User_Name, TestData.Password)
        self.homepage.do_home()
        self.newProject.do_new_project(TestData.project_name)
        self.project_overview.do_project_overview()
