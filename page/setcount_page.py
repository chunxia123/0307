import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SetCount(BaseAction):
    namebutton=By.XPATH,"//*[@text='Name']"
    phonebutton=By.XPATH,"//*[@text='Phonetic name']"
    @allure.step(title="输入用户名")
    def input_name(self,name):#输入用户名
        allure.attach("输入",name,allure.attach_type.TEXT)
        self.input(self.namebutton,name)
        allure.attach("截图",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
    @allure.step(title="输入电话")
    def input_phone(self,phone):#输入电话
        allure.attach("输入",phone,allure.attach_type.TEXT)
        self.input(self.phonebutton,phone)
