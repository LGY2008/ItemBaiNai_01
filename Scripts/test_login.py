import os,sys

import allure
import pytest

sys.path.append(os.getcwd())
# 导入统一入口类
from Page.page_in import PageIn
from Base.get_driver import get_driver
from Base.read_yml import ReadYml
# 封装读取 数据类
def get_data():
    # allure.attach("描述","开始读取数据")
    datas=ReadYml("login_data.yml").read_yml()
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect_nickname"),data.get("expect_toast")))
    return arrs
class TestLogin():
    def setup_class(self):
        # 获取driver
        self.driver=get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        # 实例化统一入口类
        self.page=PageIn(self.driver)
        # 实例化登录页面对象
        self.login=self.page.page_get_login()
        # 实例化设置页面对象
        self.setting=self.page.page_get_setting()
        # 点击我的
        self.login.page_click_me()
        # 点击已有账号去登录
        self.login.page_click_login_link()
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize("username,password,expect_nickname,expect_toast",get_data())
    @allure.step("开始登录操作")
    def test_login(self,username,password,expect_nickname,expect_toast):
        # 把登录页面对象赋值给login 便于调用
        login=self.login
        setting=self.setting
        # 如果expect_nickname不为空，说明为正向数据，执行以下步骤
        if expect_nickname:
            try:
                allure.attach("开始登录","username:%s,password%s"%(username,password))
                # 输入用户名和密码 进行登录
                login.page_login(username,password)
                # 断言是否登录成功
                assert expect_nickname in login.page_get_nickname()
                allure.attach("登录成功","username:%s,password%s"%(username,password))
                # 点击设置
                login.page_click_setting()
                allure.attach("退出操作","开始退出")
                # 点击退出
                setting.page_drag_and_drop()
                # 断言 退出是否成功
                assert setting.page_if_logout()
                allure.attach( "退出状态", "退出成功！" )
                # 点击我的
                login.page_click_me()
                # 点击已有账号
                login.page_click_login_link()
            except:
                # 截图
                login.base_get_screenshot()
        # 逆向数据(登录失败数据)执行流程
        else:
            allure.attach("开始校验类数据验证","usrename:'%s',password:'%s'"%(username,password))
            # 调用登录方法
            login.page_login( username, password )
            try:
                allure.attach("开始验证","预期toast消息为：%s"%expect_toast)
                # 断言
                assert expect_toast in login.base_get_toast(expect_toast)
                allure.attach("验证成功","预期toast：%s和捕获toast提示信息相符合"%expect_toast)
            except:
                allure.attach("开始截图","捕获toast消息与预期toast消息不符合")
                # 截图
                login.base_get_screenshot()
                img_path=os.getcwd()+os.sep+"Image"+os.sep+"faild_img.png"
                with open(img_path,"rb")as f:
                    allure.attach("截图完成，写入报告",f.read(),allure.attach_type.PNG)
                raise