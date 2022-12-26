from selene import by
import allure


def test_find(setup_browser):
    browser = setup_browser
    with allure.step("Тест поиска на странице"):
        browser.open("/")
        browser.element('.b-header-b-search-e-input').type("блокнот")
        browser.element("button.b-header-b-search-e-btn").click()


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
        browser.element('.b-header-b-search-e-input').type("848208")
        browser.element('.b-search-e-input-wrapper').click()
        browser.element('[class="btn buy-link btn-primary"]').click()
        browser.element('.b-header-b-search-e-input').type("838271")
        browser.element('.b-search-e-input-wrapper').click()
        browser.element('[class="btn buy-link btn-primary"]').click()
        browser.element('[class="b-header-b-personal-e-list-item have-dropdown  last-child have-dropdown-notouch"]').click()
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
        browser.element('[data-event-content="Школа"]').click()
        price_min = by.xpath('//input[@id="section-search-form-price_min"]')
        browser.element(price_min).type(150)
        price_max = by.xpath('//input[@id="section-search-form-price_max"]')
        browser.element(price_max).type(2500)
        show_book = by.xpath('//input[@class="btn btn-primary btn-small" and @value="Показать"]')
        browser.element(show_book).click()


def test_shipping_and_payment(setup_browser):
    browser = setup_browser
    with allure.step("Тест раздела помощи"):
        browser.open("/")
        browser.element('[data-event-content="Доставка и оплата"]').click()
        browser.element("#txtwordsadv").type("оплата qr")
        button_find = by.xpath('//input[@class="btn btn-small btn-primary" and @value="Найти"]')
        browser.element(button_find).click()

