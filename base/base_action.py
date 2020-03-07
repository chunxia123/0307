from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:
    def __init__(self,driver):
        self.driver=driver
    def find_ele(self,ele,timeout=10,poll=1):  #默认参数的位置，在最后面
        ele1,ele2=ele
        return WebDriverWait(self.driver,timeout,poll).until(lambda x :x.find_element(ele1,ele2))
    def click(self,element):
        self.find_ele(element).click()
    def input(self,ele,content):
        self.find_ele(ele).send_keys(content)
