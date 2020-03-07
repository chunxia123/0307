import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class AddPage(BaseAction):
    keepbutton=By.XPATH,"//*[@text='Keep local']"
    addbutton=By.XPATH,"//*[@text='Add account']"
    @allure.step(title='点击keeplocal')
    def click_keeplocal(self):
        self.click(self.keepbutton)

    @allure.step(title='点击添加')
    def click_addpage(self):
        self.click(self.addbutton)

