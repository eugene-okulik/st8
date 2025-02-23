import allure
import os
from final_project_lmargi.pages.const import const_login as const


@allure.feature('Login functionality')
@allure.story('Login with valid credentials')
@allure.title('Успешный вход в систему')
def test_login_ok(login_page):
    with allure.step('Open login page'):
        login_page.open_page()
    with allure.step('Accept cookies'):
        login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(os.getenv("LOGIN_PHONE"))
    login_page.set_password(os.getenv("PASSWORD"))
    login_page.click_on_submit_button()
    login_page.check_account_name_visible()
    account_name = login_page.check_account_name_visible()
    assert account_name.is_displayed(), "Account name is not visible"
    login_page.click_on_logout_button()


@allure.feature('Login functionality')
@allure.story('Login with invalid radiobutton')
@allure.title('Выбор чекбокса email вместо phone')
def test_login_error_radiobutton(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.click_on_email_button()
    login_page.set_phone(os.getenv("LOGIN_PHONE"))
    login_page.set_password(os.getenv("PASSWORD"))
    login_page.click_on_submit_button()
    login_page.check_if_radiobutton_error_visible()
    error_message_metod = login_page.check_if_radiobutton_error_visible()
    assert error_message_metod.is_displayed(), "Message invalid metod is not visible"


@allure.feature('Login functionality')
@allure.story('Invalid password error message')
@allure.title('Проверка оттображения сообщения при неверном пароле')
def test_login_invalid_password_message(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(os.getenv("LOGIN_PHONE"))
    login_page.set_password(const.INVALID_PASSWORD)
    login_page.click_on_submit_button()
    login_page.check_login_failed_message()
    error_message_login = login_page.check_login_failed_message()
    assert error_message_login.is_displayed(), "Message Login failed not visible"


@allure.feature('Login functionality')
@allure.story('Invalid phone error message')
@allure.title('Проверка оттображения сообщения при неверном номере телефона')
def test_login_invalid_phone_message(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(const.INVALID_PHONE)
    login_page.set_password(os.getenv("PASSWORD"))
    login_page.click_on_submit_button()
    login_page.check_login_failed_message()
    error_message_phone = login_page.check_login_failed_message()
    assert error_message_phone.is_displayed(), "Message invalid phone is not visible"


@allure.feature('Login functionality')
@allure.story('Error message in incorrect data')
@allure.title('Проверка оттображения сообщения при неверных данных')
def test_login_empty_data(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone('')
    login_page.set_password('')
    login_page.click_on_submit_button()
    login_page.check_invalid_phone_message()
    login_page.check_invalid_password_message()
    error_message_phone = login_page.check_invalid_phone_message()
    error_message_passw = login_page.check_invalid_password_message()

    with allure.step('Check if invalid phone error message is displayed'):
        assert error_message_phone.is_displayed(), "Message invalid phone is not visible"

    with allure.step('Check that invalid phone error message text is correct'):
        assert error_message_phone.text == const.MESSAGE_INVALID_PHONE

    with allure.step('Check if invalid password error message is displayed'):
        assert error_message_passw.is_displayed(), "Message invalid password is not visible"

    with allure.step('Check that invalid password error message text is correct'):
        assert error_message_passw.text == const.MESSAGE_INVALID_PASSW


@allure.feature('Login functionality')
@allure.story('Logout')
@allure.title('Проверка успешного выхода из системы')
def test_logout(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(os.getenv("LOGIN_PHONE"))
    login_page.set_password(os.getenv("PASSWORD"))
    login_page.click_on_submit_button()
    login_page.click_on_logout_button()
    login_page.check_login_button_visible()
    login_button = login_page.check_login_button_visible()
    assert login_button.is_displayed(), "Button Login is not visible"
