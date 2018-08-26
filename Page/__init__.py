from selenium.webdriver.common.by import By
"""
登录页面
"""
# 我
me_btn=By.ID,"com.yunmall.lc:id/tab_me"
# 已有账号,去登陆
login_link=By.ID,"com.yunmall.lc:id/textView1"
# 账号
username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 密码
password=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 登录 按钮
login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 昵称
nick_name=By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 设置
setting=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 修改密码
modify_pwd=By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 消息推送   从消息推送划到修改密码
msg_send=By.ID,"com.yunmall.lc:id/setting_notification"
# 退出按钮
logout=By.ID,"com.yunmall.lc:id/setting_logout"
# 确定退出当前账号
logout_ok=By.ID,"com.yunmall.lc:id/ymdialog_right_button"

"""
收货地址管理页面
"""
# 地址管理
address_manage=(By.ID,"com.yunmall.lc:id/setting_address_manage")
# 新增地址
new_address=By.ID,"com.yunmall.lc:id/address_add_new_btn"
# 收件人
receipt_name=By.ID,"com.yunmall.lc:id/address_receipt_name"
# 手机号
add_phone=By.ID,"com.yunmall.lc:id/address_add_phone"
# 所在地区
address_Area=By.ID,"com.yunmall.lc:id/address_province"
# 省
address_Area_sheng=By.XPATH,"//*[contains(@text,'北京')]"
# 市 外侧大框 使用class
address_Area_city_kuang=By.CLASS_NAME,"android.widget.RelativeLayout"
# 市 使用逻辑属性
address_Area_city_and=By.XPATH,"//*[contains(@text,'北京') and contains(@resource-id,'com.yunmall.lc:id/area_title')]"
# 市  注意ID是重复
address_Area_city=By.ID,"com.yunmall.lc:id/area_title"
# 区 ID和市相同
address_Area_area=By.XPATH,"//*[contains(@text,'海淀区')]"
# 详细地址
address_info=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 邮编
post_code=By.ID,"com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default=By.ID,"com.yunmall.lc:id/address_default"
# 点击保存
save_btn=By.ID,"com.yunmall.lc:id/button_send"
# 地址收件人和电话   一组元素
receipt_name_phone=By.ID,"com.yunmall.lc:id/receipt_name"
# 默认地址按钮是否存在
address_default_btn=By.ID,"com.yunmall.lc:id/address_is_default"
"""地址修改"""
# 编辑
address_edit=By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
# 保存 (保存和编辑id一样，但是不在统一界面)
address_save=By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
"""地址删除"""
delete_ok=By.ID,"com.yunmall.lc:id/ymdialog_left_button"