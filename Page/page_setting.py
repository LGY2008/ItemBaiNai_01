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