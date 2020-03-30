from selenium.webdriver.common.by import By


class AskQuestionLocators():
    BUTTON_QUESTION = [By.CSS_SELECTOR, '#btn-question'] #кнопка "задать вопрос"
    NAME = [By.CSS_SELECTOR, 'input[name="form[form_text_62]"]']
    EMAIL = [By.CSS_SELECTOR, 'input[name="form[form_text_63]"]']
    PHONE = [By.CSS_SELECTOR, 'input[name="form[form_text_64]"]']
    TEXT = [By.CSS_SELECTOR, 'textarea[name="form[form_textarea_65]"]']
    SUBMIT = [By.CSS_SELECTOR, '#form-question>button']
    FORM = [By.CSS_SELECTOR, '#form-question']