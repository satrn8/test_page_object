from selene import by
import allure


def test_find(setup_browser):
    browser = setup_browser
    with allure.step("Тест поиска на странице"):
        browser.open("/")
        browser.element('.b-header-b-search-e-input').type("блокнот")
        browser.element("button.b-header-b-search-e-btn").click()
