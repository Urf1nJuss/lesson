import pytest
from selenium import webdriver


# запуск в разных браузерах не реализован, не требуется по заданию

# задаем параметр languege, если не передан - оставляем пустым
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='',
                     help="Choose language")


# если передан параметр language подставляем в ссылку
@pytest.fixture(scope="function")
def link(request):
    language = request.config.getoption('language')
    return f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"


# открываем браузер перед запуском теста и переходим по ссылке
@pytest.fixture(scope="function")
def browser(link):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
