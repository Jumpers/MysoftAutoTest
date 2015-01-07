#-*-coding:utf-8-*-
import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

Class_CompanyCode='android.widget.TextView'#企业简称按钮class
ID_Username='com.mysoft.mobileplatform:id/et_username'#用户名id
ID_Password='com.mysoft.mobileplatform:id/et_pw'#密码id
ID_Login='com.mysoft.mobileplatform:id/button_login'#登陆按钮id
Class_CompanyCodein='android.widget.EditText'#企业简称输入框class
ID_setCompanyCodeOK='com.mysoft.mobileplatform:id/im_right_two'#企业简称界面确定按钮

Str_CompanyCode='erp306'
Str_Username='admin'
Str_Password='1'

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Android Emulator'
#         desired_caps['app'] = PATH(
#             r'D:\Git\sample-code\sample-code\apps\ContactManager\ContactManager.apk'
#         )
        desired_caps['appPackage'] = 'com.mysoft.mobileplatform'
        desired_caps['appActivity'] = 'com.mysoft.mobileplatform.activity.WelcomeActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        #输入企业代码
        self.driver.find_element_by_xpath(xpath)
        self.driver.find_element_by_class_name(Class_CompanyCode).click()
        self.driver.find_element_by_class_name(Class_CompanyCodein).clear()
        self.driver.find_element_by_class_name(Class_CompanyCodein).send_keys(Str_CompanyCode)
        self.driver.find_element_by_id(ID_setCompanyCodeOK).click()
        #输入用户名
        self.driver.find_element_by_id(ID_Username).clear()
        self.driver.find_element_by_id(ID_Username).send_keys(Str_Username)
        #输入密码
        self.driver.find_element_by_id(ID_Password).send_keys(Str_Password)
        #点击登录
        self.driver.find_element_by_id(ID_Login).click()
        
        sleep(5)
        activityName=self.driver.current_activity()
        print activityName
        
#         self.driver.refresh()


        # for some reason "save" breaks things
#         alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
#         self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

#         self.driver.press_keycode(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
