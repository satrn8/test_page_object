from selene import by
import allure


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