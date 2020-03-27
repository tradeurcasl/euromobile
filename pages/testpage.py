from .basepage import BasePage
from selenium.webdriver.common.by import By
import random
import time
from selenium.common.exceptions import NoAlertPresentException

class TestPage(BasePage):

    def should_put_a_cross(self):
        random.seed(time.time())
        number = random.random()
        button = self.browser.find_element(By.CSS_SELECTOR, 'td:nth-child('+number+')')
        button.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            button = self.browser.find_element(By.CSS_SELECTOR, 'td:nth-child(' + number + ')')
            button.click()

