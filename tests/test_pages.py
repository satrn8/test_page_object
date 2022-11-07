import time
from selene import by
import allure


def test_find(setup_browser):
    browser = setup_browser
    with allure.step("Тест поиска на странице"):
        browser.open("/")
        browser.element('[class="b-header-b-search-e-input"]').type("блокнот")
        search = by.xpath('//button[@class="b-header-b-search-e-btn"]')
        browser.element(search).click()
        time.sleep(20)


def test_click_office(setup_browser):
    browser = setup_browser
    with allure.step("Тест открытия раздела"):
        browser.open("/")
        browser.element('[href="/office/"]').click()
        browser.element('[href="/genres/2300/"]').click()


def test_id_books(setup_browser):
    browser = setup_browser
    with allure.step("Тест добавления в корзину книг по ID и заполнение формы заказа"):
        browser.open("/")
        browser.element('[class="b-header-b-search-e-input"]').type("848208")
        browser.element('[class="b-search-e-input-wrapper"]').click()
        browser.element('[class="btn buy-link btn-primary"]').click()
        browser.element('[class="b-header-b-search-e-input"]').type("838271")
        browser.element('[class="b-search-e-input-wrapper"]').click()
        browser.element('[class="btn buy-link btn-primary"]').click()
        browser.element('[class="b-header-b-personal-e-list-item have-dropdown  last-child have-dropdown-notouch"]').click()
        browser.config.timeout = 20
        browser.element('[class="btn btn-primary btn-large fright start-checkout-js"]').click()

        first_name = by.xpath('//input[@placeholder="Имя"]')
        browser.element(first_name).type("Алёна")
        last_name = by.xpath('//input[@placeholder="Фамилия"]')
        browser.element(last_name).type("Иванова")
        user_number = by.xpath('//input[@placeholder="Мобильный телефон"]')
        browser.element(user_number).type("89998555611")
        user_email = by.xpath('//input[@placeholder="Электронная почта"]')
        browser.element(user_email).type("test@test.ru")


def test_school(setup_browser):
    browser = setup_browser
    with allure.step("Тест фильтрации по диапазону цены"):
        browser.open("/")
        school = by.xpath('//li[@class="b-header-b-menu-e-list-item b-toggle b-header-b-menu-e-list-item-m-temp analytics-click-js"][1]')
        browser.element(school).click()
        price_min = by.xpath('//input[@id="section-search-form-price_min"]')
        browser.element(price_min).type(150)
        price_max = by.xpath('//input[@id="section-search-form-price_max"]')
        browser.element(price_max).type(2500)
        show_book = by.xpath('//input[@class="btn btn-primary btn-small" and @value="Показать"]')
        browser.element(show_book).click()
        browser.config.timeout = 100


def test_shipping_and_payment(setup_browser):
    browser = setup_browser
    with allure.step("Тест раздела помощи"):
        browser.open("/")
        button_shipping_and_payment = ('//li[@class="b-header-b-sec-menu-e-list-item first-child analytics-click-js" and @data-event-content="Доставка и оплата"]')
        browser.element(button_shipping_and_payment).click()
        browser.element("#txtwordsadv").type("оплата qr")
        button_find = by.xpath('//input[@class="btn btn-small btn-primary" and @value="Найти"]')
        browser.element(button_find).click()

