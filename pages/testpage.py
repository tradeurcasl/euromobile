from .basepage import BasePage
from .locators import CommercialOfferLocators
from .locators import AskQuestionLocators
from .locators import OrderCalculationLocators
from ..settings import name, email, phone, message, item, quantity


class SuitPage(BasePage):

    def should_ask_question_product_page(self):
        button = self.browser.find_element(*AskQuestionLocators.BUTTON_QUESTION)
        button.click()
        input1 = self.browser.find_element(*AskQuestionLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*AskQuestionLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*AskQuestionLocators.PHONE)
        input3.send_keys(phone)
        input4 = self.browser.find_element(*AskQuestionLocators.TEXT)
        input4.send_keys(message)
        button = self.browser.find_element(*AskQuestionLocators.SUBMIT)
        button.click()
        self.is_disappeared(*AskQuestionLocators.FORM)
        assert True, 'Form did not send'

    def should_commercial_offer(self):
        button = self.browser.find_element(*CommercialOfferLocators.BUTTON_OFFER)
        button.click()
        input1 = self.browser.find_element(*CommercialOfferLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*CommercialOfferLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*CommercialOfferLocators.PHONE)
        input3.send_keys(phone)
        input4 = self.browser.find_element(*CommercialOfferLocators.TEXT)
        input4.send_keys(message)
        button = self.browser.find_element(*CommercialOfferLocators.SUBMIT)
        button.click()
        self.is_disappeared(*CommercialOfferLocators.FORM)
        assert True, 'Form did not send'

    def should_order_calculation(self):

        button = self.browser.find_element(*OrderCalculationLocators.BUTTON_CALC)
        button.click()
        input1 = self.browser.find_element(*OrderCalculationLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*OrderCalculationLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*OrderCalculationLocators.PHONE)
        input3.send_keys(phone)
        input6 = self.browser.find_element(*OrderCalculationLocators.ITEM)
        input6.send_keys(item)
        input6 = self.browser.find_element(*OrderCalculationLocators.QUANTITY)
        input6.send_keys(quantity)
        input6 = self.browser.find_element(*OrderCalculationLocators.TEXT)
        input6.send_keys(message)
        button = self.browser.find_element(*OrderCalculationLocators.SUBMIT)
        button.click()
        self.is_disappeared(*OrderCalculationLocators.FORM)
        assert True, 'Form did not send'