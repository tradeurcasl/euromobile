#from .pages.basepage import BasePage
from .pages.testpage import SuitPage
from .settings import link, linkprice, linkservice, linkcontact, linksolution, linkorder
import pytest

class TestWebForms():

    
    def test_ask_question_product_page(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_ask_question_product_page()


    def test_commercial_offer(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_commercial_offer()


    def test_order_calculation(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_order_calculation()


    def test_want_to_know_price(self, browser):
        page = SuitPage(browser, linkprice)
        page.open()
        page.should_know_price()


    def test_order_service(self, browser):
        page = SuitPage(browser, linkservice)
        page.open()
        page.should_order_service()


    def test_feedback(self, browser):
        page = SuitPage(browser, linkcontact)
        page.open()
        page.should_be_feedback()


    def test_solution(self, browser):
        page = SuitPage(browser, linksolution)
        page.open()
        page.should_order_solution()

    def test_order_product(self, browser):
        page = SuitPage(browser, linkorder)
        page.open()
        page.should_order_product()