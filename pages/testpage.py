from .basepage import BasePage
from .locators import CommercialOfferLocators, AskQuestionLocators, OrderCalculationLocators, KnowPriceLocators
from .locators import ServiceLocators, FeedbackLocators
from ..settings import name, email, phone, message, item, quantity, object, company


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

    def should_know_price(self):
        button = self.browser.find_element(*KnowPriceLocators.BUTTON_PRICE)
        button.click()
        input1 = self.browser.find_element(*KnowPriceLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*KnowPriceLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*KnowPriceLocators.PHONE)
        input3.send_keys(phone)
        button = self.browser.find_element(*KnowPriceLocators.SUBMIT)
        button.click()
        self.is_disappeared(*KnowPriceLocators.FORM)
        assert True, 'Form did not send'

    def should_order_service(self):
        self.browser.set_window_size(1920, 768)
        self.browser.execute_script("window.scrollTo(0, 200)")
        button = self.browser.find_element(*ServiceLocators.BUTTON_SERVE)
        button.click()
        input1 = self.browser.find_element(*ServiceLocators.NAME)
        input1.send_keys(name)
        input0 = self.browser.find_element(*ServiceLocators.COMPANY)
        input0.send_keys(company)
        input2 = self.browser.find_element(*ServiceLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*ServiceLocators.PHONE)
        input3.send_keys(phone)
        input6 = self.browser.find_element(*ServiceLocators.TYPE_OF_OBJECT)
        input6.send_keys(object)
        input6 = self.browser.find_element(*ServiceLocators.QUANTITY)
        input6.send_keys(quantity)
        input6 = self.browser.find_element(*ServiceLocators.TEXT)
        input6.send_keys(message)
        self.browser.find_element(*ServiceLocators.CHECKBOX).click()
        button = self.browser.find_element(*ServiceLocators.SUBMIT)
        button.click()
        self.is_disappeared(*ServiceLocators.FORM)
        assert True, 'Form did not send'

    def should_be_feedback(self):
        self.browser.execute_script("window.scrollTo(0, 1000)")
        input1 = self.browser.find_element(*FeedbackLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*FeedbackLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*FeedbackLocators.PHONE)
        input3.send_keys(phone)
        input6 = self.browser.find_element(*FeedbackLocators.TEXT)
        input6.send_keys(message)
        button = self.browser.find_element(*FeedbackLocators.SUBMIT)
        button.click()
        self.is_disappeared(*FeedbackLocators.SUCCESS)
        assert True, 'Form did not send'