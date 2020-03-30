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
    BUTTON_CALC = [By.CSS_SELECTOR, '#btn-calculation']
    NAME = [By.CSS_SELECTOR, '#calc-name']
    EMAIL = [By.CSS_SELECTOR, '#calc-email']
    PHONE = [By.CSS_SELECTOR, '#calc-phone']
    ITEM = [By.CSS_SELECTOR, '#calc-item']
    QUANTITY = [By.CSS_SELECTOR, '#calc-quantity']
    TEXT = [By.CSS_SELECTOR, '#calc-text']
    SUBMIT = [By.CSS_SELECTOR, '#form-calc>button']
    FORM = [By.CSS_SELECTOR, '#form-calc']