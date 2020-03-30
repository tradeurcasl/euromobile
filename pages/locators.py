from selenium.webdriver.common.by import By


class AskQuestionLocators():
    BUTTON_QUESTION = [By.CSS_SELECTOR, '#btn-question'] #кнопка "задать вопрос"
    NAME = [By.CSS_SELECTOR, 'input[name="form[form_text_62]"]']
    EMAIL = [By.CSS_SELECTOR, 'input[name="form[form_text_63]"]']
    PHONE = [By.CSS_SELECTOR, 'input[name="form[form_text_64]"]']
    TEXT = [By.CSS_SELECTOR, 'textarea[name="form[form_textarea_65]"]']
    SUBMIT = [By.CSS_SELECTOR, '#form-question>button']
    FORM = [By.CSS_SELECTOR, '#form-question']

class CommercialOfferLocators():
    '''Опять же, как появятся новые формы, заменяем селекторы на них. В баттон-офере можно заменить на сss,
    просто на данном этапе икспас выглядит симпатичнее (ага, вот эта бандура), чем ксс'''
    BUTTON_OFFER = [By.XPATH, '//*[@id="container"]/main/div[1]/section[3]/div/div[3]/button']
    NAME = [By.CSS_SELECTOR, 'input[name="form[form_text_71]"]']
    EMAIL = [By.CSS_SELECTOR, 'input[name="form[form_text_72]"]']
    PHONE = [By.CSS_SELECTOR, 'input[name="form[form_text_73]"]']
    TEXT = [By.CSS_SELECTOR, 'textarea[name="form[form_textarea_75]"]']
    SUBMIT = [By.CSS_SELECTOR, '#form-offer>button']
    FORM = [By.CSS_SELECTOR, '#form-offer']

class OrderCalculationLocators():
    '''Это форма заказа расчета. Тут очень удобные айдишники, поэтому все выглядит красивее. При возможности,
    лучше использовать подобную маркировку элементов'''
    BUTTON_CALC = [By.CSS_SELECTOR, '#btn-calculation']
    NAME = [By.CSS_SELECTOR, '#calc-name']
    EMAIL = [By.CSS_SELECTOR, '#calc-email']
    PHONE = [By.CSS_SELECTOR, '#calc-phone']
    ITEM = [By.CSS_SELECTOR, '#calc-item']
    QUANTITY = [By.CSS_SELECTOR, '#calc-quantity']
    TEXT = [By.CSS_SELECTOR, '#calc-text']
    SUBMIT = [By.CSS_SELECTOR, '#form-calc>button']
    FORM = [By.CSS_SELECTOR, '#form-calc']

class KnowPriceLocators():
    '''Запрос стоимости товара из общего каталога. Да, тут опять икспас, потому что ксс еще более громоздкий'''
    BUTTON_PRICE = [By.XPATH, '//*[@id="tabs-all"]/div/div[2]/div/span[2]']
    NAME = [By.CSS_SELECTOR, 'input[name="form[form_text_67]"]']
    EMAIL = [By.CSS_SELECTOR, 'input[name="form[form_text_68]"]']
    PHONE = [By.CSS_SELECTOR, 'input[name="form[form_text_69]"]']
    SUBMIT = [By.CSS_SELECTOR, '#form-price>button']
    FORM = [By.CSS_SELECTOR, '#form-price']

class ServiceLocators():
    '''Это на странице сервиса заказать обслуживание'''
    BUTTON_SERVE = [By.XPATH, '//*[@id="container"]/main/div[1]/div/div[3]/a']
    COMPANY = [By.CSS_SELECTOR, 'input[name="form[form_text_97]"]']
    NAME = [By.CSS_SELECTOR, 'input[name="form[form_text_96]"]']
    EMAIL = [By.CSS_SELECTOR, 'input[name="form[form_text_98]"]']
    PHONE = [By.CSS_SELECTOR, 'input[name="form[form_text_99]"]']
    TYPE_OF_OBJECT = [By.CSS_SELECTOR, 'input[name="form[form_text_100]"]']
    QUANTITY = [By.CSS_SELECTOR, 'input[name="form[form_text_101]"]']
    TEXT = [By.CSS_SELECTOR, 'textarea[name="form[form_textarea_102]"]']
    SUBMIT = [By.CSS_SELECTOR, '#form-request>button']
    FORM = [By.CSS_SELECTOR, '#form-request']
    CHECKBOX = [By.CSS_SELECTOR, '#check-question']
