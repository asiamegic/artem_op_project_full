import pytest
from pytestUi.test_base import BaseTest
from Pages.home_page import HomePage
from Pages.login_page import Login
from Pages.new_work_package_page import New_Work_Package
from Pages.project_overview import Project
from config.config import TestData
import time


class Test_Automation_Task(BaseTest):

    def test_Ui_CreateTask(self):
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.home = HomePage(self.driver)
        self.newWorkProject = New_Work_Package(self.driver)
        self.project_overview = Project(self.driver)
        self.login.do_login(TestData.User_Name, TestData.Password)
        self.home.do_home1(TestData.projectName)
        self.newWorkProject.do_work(TestData.package_name, TestData.package_des)
        self.project_overview.do_project_overview1()
