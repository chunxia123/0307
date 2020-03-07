from base.base_action import BaseAction
from page.add_page import AddPage
from page.choose_page import ChoosePage
from page.contact import Contact
from page.serversetting_page import ServerSetting
from page.setcount2_page import SetCount2
from page.setcount_page import SetCount


class Page:
    def __init__(self,driver):
        self.driver=driver
    def contact(self):
        return Contact(self.driver)#易错，忘记了传driver
    def add_page(self):
        return AddPage(self.driver)
    def choose_page(self):
        return ChoosePage(self.driver)
    def serversetting_page(self):
        return ServerSetting(self.driver)
    def setcount2(self):
        return SetCount2(self.driver)
    def setcount(self):
        return SetCount(self.driver)
