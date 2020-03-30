#from .pages.basepage import BasePage
from .pages.testpage import SuitPage
from .settings import link

class TestWebForms():

    def test_ask_question_product_page(self, browser):
        page = SuitPage(browser, link)
        page.open()
        page.should_ask_question_product_page()