from selene import by
import allure


def test_click_office(setup_browser):
    browser = setup_browser
    with allure.step("Тест открытия раздела"):
        browser.open("/")
        browser.element('[href="/office/"]').click()
        browser.element('[href="/genres/2300/"]').click()