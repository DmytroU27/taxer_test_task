from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_PROJECT_BUTTON = (By.CSS_SELECTOR, "button")
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    CANCEL_BUTTON = (By.CSS_SELECTOR, ".btn-secondary")
    DROPBOX = (By.CSS_SELECTOR, ".dropbox")
    CERT_IN_LIST = (By.CSS_SELECTOR, ".list-group-item")
    COMMON_NAME_DATA = (By.CSS_SELECTOR, ".table-borderless tr:first-child td")
    ISSUER_CN_DATA = (By.CSS_SELECTOR, ".table-borderless tr:nth-child(2) td")
    VALID_FROM_DATA = (By.CSS_SELECTOR, ".table-borderless tr:nth-child(3) td")
    VALID_TILL_DATA = (By.CSS_SELECTOR, ".table-borderless tr:last-child td")
