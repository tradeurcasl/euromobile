#from .pages.basepage import BasePage
from .pages.testpage import SuitPage
from .settings import link
import pytest

class TestWebForms():

    @pytest.mark.skip
    def test_ask_question_product_page(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_ask_question_product_page()

    def test_commercial_offer(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_commercial_offer()