from selenium.webdriver.common.by import By
import time

def test_button_add_to_basket_exists(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert len(buttons) > 0, 'busket button not found'
