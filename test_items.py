from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_avail_button(browser):
    WebDriverWait(browser, 6).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")))
    element = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert element     # проверяем, что кнопка есть на странице

