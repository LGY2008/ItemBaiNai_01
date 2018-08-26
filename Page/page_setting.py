import Page
from Base.base import Base
class PageSetting(Base):
    # 退出登录
    def page_drag_and_drop(self):
        # 消息推送
        msg_send=self.base_find_element(Page.msg_send)
        # 修改密码
        modify_pwd=self.base_find_element(Page.modify_pwd)
        # 调用 滑动方法  从消息推送划到修改密码
        self.base_drag_and_drop(msg_send,modify_pwd)
        # 点击退出
        self.base_click(Page.logout)
        # 点击确定退出当前账号
        self.base_click(Page.logout_ok)
    # 判断是否退出成功
    def page_if_logout(self):
        try:
            # 查找我
            self.base_find_element(Page.me_btn)
            # 找到我，说明退出成功，返回True
            return True
        except:
            # 异常，说明退出失败，返回False
            return False
    # 点击地址管理
    def page_click_address_manage(self):
        self.base_click(Page.address_manage)
    # 新增地址 按钮
    def page_click_new_address(self):
        self.base_click(Page.new_address)
    # 收件人
    def page_input_receipt_name(self,text="张三"):
        self.base_input_text(Page.receipt_name,text)
    # 手机号
    def page_input_phone(self,phone="18688888888"):
        self.base_input_text(Page.add_phone,phone)
    # 所在区域
    def page_select_Area(self):
        # 点击所在地区
        self.base_click(Page.address_Area)
        # 点击 北京市
        self.base_click(Page.address_Area_sheng)
        # 点击 北京市 大框
        self.base_click(Page.address_Area_city_kuang)
        # 点击 北京市
        self.base_click(Page.address_Area_city)
        # 点击 区域
        self.base_click(Page.address_Area_area)
    # 详细地址
    def page_input_address_info(self,text="清河三街93号"):
        self.base_input_text(Page.address_info,text)
    # 邮编
    def page_input_post_code(self,post="100080"):
        self.base_input_text( Page.post_code, post )
    # 默认地址
    def page_click_default_address(self):
        self.base_click( Page.address_default )
    # 点击保存
    def page_click_save_btn(self):
        self.base_click(Page.save_btn)
    # 所在区域
    def page_select_Area_xpath(self,sheng="广东",shi="深圳",qu="宝安"):
        # 点击所在地区
        self.base_click(Page.address_Area)
        # 点击 省份
        self.base_click_xpath(sheng)
        # 点击 市
        self.base_click_xpath( shi )
        # 点击 区域
        self.base_click_xpath( qu )
    # 断言 获取地址列表 收件人和电话
    def page_get_receipt_name_phone(self):
        elements=self.base_find_elements(Page.receipt_name_phone)
        return [i.text for i in elements]
    # 断言是否有默认地址
    def page_if_default(self):
        try:
            self.base_find_element(Page.address_default_btn)
            # 不报异常，返回True说明找到默认按钮
            return True
        except:
            # 返回False，没有找到默认按钮
            return False
    # 返回xpath符合条件的所有列表元素   修改 、删除
    def page_get_elements(self,text):
        return self.base_xpath_return_elements(text)

    # 点击列表固定元素
    def page_click_elements(self,text):
        self.base_click_elements(self.page_get_elements(text))
    # 点击编辑
    def page_click_edit_btn(self):
        self.base_click(Page.address_edit)

    # 修改地址 封装
    def page_edit_address(self,receipt_name,phone,sheng,shi,qu,address_info,post):
        # 修改收件人
        self.page_input_receipt_name(receipt_name)
        # 修改手机号
        self.page_input_phone(phone)
        # 修改所在地区
        self.page_select_Area_xpath(sheng,shi,qu)
        # 修改详细地址
        self.page_input_address_info(address_info)
        # 修改邮编
        self.page_input_post_code(post)
        # 点击保存
        self.base_click_xpath("保存")

    # 循环删除地址 封装
    def page_delete_address(self,text="删除"):
        # 获取地址列表 长度 循环删除的次数
        address_list=self.page_get_receipt_name_phone()
        for i in range(len(address_list)):
            # 获取删除所有列表元素  (每次遍历获取最新列表)
            del_element=self.page_get_elements(text)
            # 把元素列表传入 元素点击方法 默认点击元素列表下标为0的元素
            self.base_click_elements(del_element)
            # 点击确认删除
            self.base_click(Page.delete_ok)
            # 点击编辑
            self.page_click_edit_btn()
    # 删除断言 封装
    def if_delete_none(self):
        """返回False说明删除失败，返回True说明删除成功！地址列表已无地址"""
        try:
            # 查找元素列表
            self.page_get_receipt_name_phone()
            return False
        except:
            return True