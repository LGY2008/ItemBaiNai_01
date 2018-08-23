from Page.page_login import PageLogin
from Page.page_setting import PageSetting
class PageIn():
    def __init__(self,driver):
        self.driver=driver
    # 定义 登录页面对象类
    def page_get_login(self):
        return PageLogin(self.driver)
    # 定义 设置页面对象类
    def page_get_setting(self):
        return PageSetting(self.driver)