from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button, "No add to basket button"

# pytest --language=es
# pytest --language=fr test_items.py
# pytest --browser_name=firefox --language=ru test_items.py
# pytest --language=en test_items.py
