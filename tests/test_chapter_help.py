from selene import by
import allure


def test_shipping_and_payment(setup_browser):
    browser = setup_browser
    with allure.step("Тест раздела помощи"):
        browser.open("/")
        browser.element('[data-event-content="Доставка и оплата"]').click()
        browser.element("#txtwordsadv").type("оплата qr")
        button_find = by.xpath('//input[@class="btn btn-small btn-primary" and @value="Найти"]')
        browser.element(button_find).click()

