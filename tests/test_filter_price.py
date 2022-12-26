from selene import by
import allure


def test_school(setup_browser):
    browser = setup_browser
    with allure.step("Тест фильтрации по диапазону цены"):
        browser.open("/")
        browser.element('[data-event-content="Школа"]').click()
        price_min = by.xpath('//input[@id="section-search-form-price_min"]')
        browser.element(price_min).type(150)
        price_max = by.xpath('//input[@id="section-search-form-price_max"]')
        browser.element(price_max).type(2500)
        show_book = by.xpath('//input[@class="btn btn-primary btn-small" and @value="Показать"]')
        browser.element(show_book).click()
