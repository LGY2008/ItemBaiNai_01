import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化
    def __init__(self,driver):
        self.driver=driver
    # 定位元素--单个
    def base_find_element(self,loc,timout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout=timout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 定位元素--list
    def base_find_elements(self, loc, timout=10, poll=0.5):
        return WebDriverWait( self.driver, timeout=timout, poll_frequency=poll ).until( lambda x: x.find_elements( *loc ) )
    # 点击元素方法
    def base_click(self,loc):
        """
        :param loc:元组：By.XPATH,元素位置
        """
        self.base_find_element(loc).click()
    # 给元素输入文本
    def base_input_text(self,loc,text):
        # 获取元素
        el=self.base_find_element(loc)
        # 清空数据
        el.clear()
        # 输入数据
        el.send_keys(text)
    # 截屏
    def base_get_screenshot(self):
        # 动态获取图片目录
        path=os.getcwd()+os.sep+"Image"+os.sep+"faild_img.png"
        # 调用截图方法
        self.driver.get_screenshot_as_file(path)
    # 获取toast
    def base_get_toast(self,message):
        """
        :param message: 为模糊匹配的信息
        :return: 获取的toast信息
        """
        message="//*[contains(@text,'"+message+"')]"
        return self.base_find_element((By.XPATH,message),poll=0.01).text
    # 获取文本信息
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 滑动元素
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)
    # 使用xpath点击 封装
    def base_xpath_click(self,message):
        message = "//*[contains(@text,'" + message + "')]"
        self.base_find_element((By.XPATH,message)).click()
    # 第二次演示封装
    def base_click_xpath(self,message):
        message="//*[contains(@text,'"+message+"')]"
        self.base_find_element((By.XPATH,message)).click()
    # 封装 根据传入字符串，返回符合条件的元素列表
    def base_xpath_return_elements(self,text):
        text = "//*[contains(@text,'" + text + "')]"
        return self.base_find_elements((By.XPATH,text))
    # 传入元素列表，进行固定点击操作
    def base_click_elements(self,elements):
        elements[0].click()