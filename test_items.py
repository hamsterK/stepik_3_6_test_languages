from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, '.add-to-basket')
    assert len(add_to_basket_button), 'Add to basket button is missing'


