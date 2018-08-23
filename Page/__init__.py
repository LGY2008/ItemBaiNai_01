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