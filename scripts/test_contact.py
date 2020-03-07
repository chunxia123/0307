from base.base_driver import initdriver
from base.read_data import read_yaml
from page.page import Page
import pytest


class TestContact:
    def setup(self):
        self.driver=initdriver()
        self.page=Page(self.driver)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("args",read_yaml("test_content1","contact_data.yaml"))
    #def test_contact(self,name,phone):
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_contact1(self,args):
        print(args)
        print(args["name"])
        self.page.contact().click_contact()
        self.page.add_page().click_keeplocal()
        self.page.setcount().input_name(args["name"])
        self.page.setcount().input_phone(args["phone"])



   # @pytest.mark.parametrize(("name", "phone"), [("wang", 121), ("li", 333)])
    #def test_contact2(self):



