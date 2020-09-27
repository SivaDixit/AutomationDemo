import time

from ElementHelper import ElementHelper
from selenium.webdriver.common.by import By
import sys

from selenium.webdriver.common.keys import Keys


sys.path.append("../../")
from utilities.baseclass import baseClass


class NaukriLogin(ElementHelper):
    global driver
    #web elements
    search = "q"
    naukri_link = "//*[contains(@href,'https://www.naukri.com/')]"
    login = "//*[contains(@title,'Jobseeker') and contains(@title,'Login')]"
    naukri_username = "//input[contains(@type,'text') and contains(@placeholder,'Username')]"
    naukri_password = "//input[contains(@type,'password')]"
    login_submit = "//*[@type='submit']"

    def __init__(self,driver):

        self.driver = driver

    def enter_text_in_google_search(self,text):

        self.driver.find_element_by_name(self.search).send_keys(text)
        return self.driver.find_element_by_name(self.search).send_keys(Keys.ENTER)

    def login_naukri(self,username,password):
        self.clickElementXpath(self.driver,self.naukri_link)
        self.clickElementXpath(self.driver,self.login)
        self.enterKeysInTextBoxXpath(self.driver,self.naukri_username,username)
        self.enterKeysInTextBoxXpath(self.driver,self.naukri_password,password)
        return self.clickElementXpath(self.driver,self.login_submit)
         # self.driver.find_element_by_xpath(self.naukri_link).click()
         # self.driver.find_element_by_xpath(self.login).click()
         # self.driver.find_element_by_xpath(self.naukri_username).send_keys(username)
         # self.driver.find_element_by_xpath(self.naukri_password).send_keys(password)
         # time.sleep(3)
         # self.driver.find_element_by_xpath(self.login_submit).click()
         # return time.sleep(3)


