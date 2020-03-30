#from .pages.basepage import BasePage
from .pages.testpage import SuitPage
from .settings import link, linkprice, linkservice, linkcontact, linksolution
import pytest

class TestWebForms():

    @pytest.mark.skip
    def test_ask_question_product_page(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_ask_question_product_page()

    @pytest.mark.skip
    def test_commercial_offer(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_commercial_offer()

    @pytest.mark.skip
    def test_order_calculation(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_order_calculation()

    @pytest.mark.skip
    def test_want_to_know_price(self, browser):
        page = SuitPage(browser, linkprice)
        page.open()
        page.should_know_price()

    @pytest.mark.skip
    def test_order_service(self, browser):
        page = SuitPage(browser, linkservice)
        page.open()
        page.should_order_service()

    @pytest.mark.skip
    def test_feedback(self, browser):
        page = SuitPage(browser, linkcontact)
        page.open()
        page.should_be_feedback()

    def test_solution(self, browser):
        page = SuitPage(browser, linksolution)
        page.open()
        page.should_order_solution()