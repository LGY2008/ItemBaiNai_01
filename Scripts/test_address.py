import os,sys
import allure
import pytest
sys.path.append(os.getcwd())
from Base.read_yml import ReadYml
from Page.page_in import PageIn
from Base.get_driver import get_driver
# 读取数据
def get_data(text):
    if text=="add":
        datas=ReadYml("address_data.yml").read_yml()
        arrs=[]
        for data in datas.get("add_address").values():
            arrs.append((data.get("receipt_name"),data.get("phone"),data.get("address_info"),data.get("post")))
        return arrs
    elif text=="edit":
        datas=ReadYml("address_data.yml").read_yml()
        arrs=[]
        for data in datas.get("edit_address").values():
            arrs.append((data.get("text"),data.get("receipt_name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("address_info"),data.get("post")))
        return arrs

# 读取数据
# def get_data():
#     datas=ReadYml("address_data.yml").read_yml()
#     arrs=[]
#     for data in datas.values():
#         arrs.append((data.get("receipt_name"),data.get("phone"),data.get("address_info"),data.get("post")))
#     return arrs
class TestAddress():
    @allure.step("初始化操作")
    def setup_class(self):
        print("获取数据驱动的添加地址格式：",get_data("add"))
        print( "获取数据驱动的编辑址格式：", get_data( "edit" ) )
        # 获取driver
        self.driver=get_driver()
        # 获取统一入口类
        self.page=PageIn(self.driver)
        # 获取设置页面对象
        self.setting=self.page.page_get_setting()
        allure.attach("描述","地址管理前登陆")
        # 登录 +点击设置
        self.page.page_get_login().page_login_address()
        allure.attach( "描述", "点击地址管理" )
        # 点击地址管理
        self.setting.page_click_address_manage()
    def teardown_class(self):
       # 关闭driver
       self.driver.quit()

    @pytest.mark.run( order=1 )
    @pytest.mark.parametrize("receipt_name,phone,address_info,post",get_data("add"))
    def test_add_address(self,receipt_name,phone,address_info,post):
        allure.attach( "描述", "点击新增地址" )
        # 点击新增地址
        self.setting.page_click_new_address()
        allure.attach( "描述", "输入收件人" )
        # 输入收件人
        self.setting.page_input_receipt_name(receipt_name)
        allure.attach( "描述", "输入手机号" )
        # 输入手机号
        self.setting.page_input_phone(phone)
        allure.attach( "描述", "选择所在区域" )
        # 所在区域
        # self.setting.page_select_Area()
        self.setting.page_select_Area_xpath()
        allure.attach( "描述", "输入详细地址" )
        # 详细地址
        self.setting.page_input_address_info(address_info)
        allure.attach( "描述", "输入邮编" )
        # 邮编
        self.setting.page_input_post_code(post)
        allure.attach( "描述", "设为默认地址" )
        # 默认地址
        self.setting.page_click_default_address()
        allure.attach( "描述", "点击保存按钮" )
        # 点击保存按钮
        self.setting.page_click_save_btn()
        try:
            allure.attach( "描述", "开始判断地址是否添加成功" )
            # 断言地址是否添加成功
            receipt_name_phone=receipt_name+'  '+phone
            assert receipt_name_phone in self.setting.page_get_receipt_name_phone()
            allure.attach( "描述", "地址添加成功" )
            allure.attach( "描述", "判断是否有默认按钮" )
            # 判断是否有默认按钮
            assert self.setting.page_if_default()
        except:
            allure.attach( "描述", "添加地址或默认地址失败" )
            allure.attach( "描述", "开始截图" )
            # 截图
            self.setting.base_get_screenshot()
            img_path = os.getcwd() + os.sep + "Image" + os.sep + "faild_img.png"
            with open( img_path, "rb" )as f:
                allure.attach( "截图完成，写入报告", f.read(), allure.attach_type.PNG )
            allure.attach( "描述", "截图成功，并导入报告" )
            raise

    # 修改地址
    @pytest.mark.run( order=2 )
    @allure.step("修改地址")
    @pytest.mark.parametrize("text,receipt_name,phone,sheng,shi,qu,address_info,post",get_data("edit"))
    def test_edit_address(self,text,receipt_name,phone,sheng,shi,qu,address_info,post):
        # 点击编辑
        self.setting.page_click_edit_btn()
        # 点击修改按钮
        self.setting.page_click_elements(text)
        # 修改地址
        self.setting.page_edit_address(receipt_name,phone,sheng,shi,qu,address_info,post)
        try:
            # 断言
            receipt_name_phone=receipt_name+"  "+phone
            assert receipt_name_phone in self.setting.page_get_receipt_name_phone()
            allure.attach( "描述：", "修改地址成功！" )
        except:
            allure.attach("描述：","修改地址失败！")
            # 截图
            self.setting.base_get_screenshot()
            img_path = os.getcwd() + os.sep + "Image" + os.sep + "faild_img.png"
            with open( img_path, "rb" )as f:
                allure.attach( "截图完成，写入报告", f.read(), allure.attach_type.PNG )
            allure.attach( "描述", "截图成功，并导入报告" )
            raise

    # 删除地址
    @pytest.mark.run( order=3 )
    def test_delete_address(self):
        # 点击 编辑按钮
        self.setting.page_click_edit_btn()
        # 删除
        self.setting.page_delete_address()
        try:
            # 断言
            assert self.setting.if_delete_none()
            allure.attach( "描述：", "删除地址地址！" )
        except:
            allure.attach("描述：","删除地址失败！")
            # 截图
            self.setting.base_get_screenshot()
            img_path = os.getcwd() + os.sep + "Image" + os.sep + "faild_img.png"
            with open( img_path, "rb" )as f:
                allure.attach( "截图完成，写入报告", f.read(), allure.attach_type.PNG )
            allure.attach( "描述", "截图成功，并导入报告" )
            raise
