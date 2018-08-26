from Base.base import Base
import Page
class PageLogin(Base):
    # 点击 我
    def page_click_me(self):
        self.base_click(Page.me_btn)
    # 点击已有账号去登录
    def page_click_login_link(self):
        self.base_click(Page.login_link)
    # 输入账号
    def page_input_username(self,username):
        self.base_input_text(Page.username,username)
    # 输入密码
    def page_input_password(self,password):
        self.base_input_text(Page.password,password)
    # 点击登录
    def page_click_login(self):
        self.base_click(Page.login_btn)
    # 获取登录后的信息 昵称
    def page_get_nickname(self):
        return self.base_get_text(Page.nick_name)
    # 点击设置
    def page_click_setting(self):
        self.base_click(Page.setting)
    # 封装登录 方法
    def page_login(self,username,password):
        # 输入账号和密码
        self.page_input_username(username)
        self.page_input_password(password)
        # 点击登录
        self.page_click_login()

    # 登录封装二 地址管理初始化专用
    def page_login_address(self,username="18610453007",password="123456"):
        # 点击 我
        self.page_click_me()
        # 已有账号去登录
        self.page_click_login_link()
        # 输入账号和密码
        self.page_input_username(username)
        self.page_input_password(password)
        # 点击登录
        self.page_click_login()
        # 点击设置
        self.page_click_setting()