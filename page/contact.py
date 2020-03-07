import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class Contact(BaseAction):
    addbutton=(By.ID,"com.android.contacts:id/floating_action_button")
    @allure.step(title="点击添加联系人")
    def click_contact(self):#点击添加联系人
        self.click(self.addbutton)