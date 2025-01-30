
from final_project_lmargi.pages.const import const_login as const
import  time

# Авторизация/Логин (7 тестов):
#сделаны:
# Проверка корректности логина (положительный сценарий).
# Проверка с некорректной радио кнопкой (вместо телефона, выбрана почта).
# Проверка с неправильными учетными данными  и сообщением о неуспешном входе
# Проверка на правильность вывода сообщения при вводе неверного пароля.


# нет:
# Проверка с пустыми полями логина.
# Проверка восстановления пароля.
# Проверка выхода из аккаунта (Logout).

# 21 test ok
def login_ok(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(const.LOGON_PHONE)
    login_page.set_password(const.PASSWORD)
    login_page.click_on_submit_button()
    login_page.check_account_name_visible()
    account_name = login_page.check_account_name_visible()
    assert account_name.is_displayed(), "Account name is not visible"

# 22 test ok
def login_error_radiobutton(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.click_on_email_button()
    login_page.set_phone(const.LOGON_PHONE)
    login_page.set_password(const.PASSWORD)
    login_page.click_on_submit_button()
    login_page.check_if_radiobutton_error_visible()
    error_message_metod = login_page.check_if_radiobutton_error_visible()
    assert error_message_metod.is_displayed(), "Message invalid metod is not visible"


# 23 test ok
def login_invalid_password_message(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(const.LOGON_PHONE)
    login_page.set_password(const.INVALID_PASSWORD)

    login_page.click_on_submit_button()
    login_page.check_login_failed_message()
    error_message_login = login_page.check_login_failed_message()
    assert error_message_login.is_displayed(), "Message Login failed not visible"



def login_invalid_phone_message(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(const.INVALID_PHONE)
    time.sleep(2)
    login_page.set_password(const.PASSWORD)
    login_page.click_on_submit_button()
    login_page.check_invalid_phone_message()
    error_message_phone = login_page.check_invalid_phone_message()
    assert error_message_phone.is_displayed(), "Message invalid phone is not visible"
    assert error_message_phone.text == 'Въведете валиден мобилен Мобилен телефон'

# 25 test OK
def login_empty_data(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone('')
    login_page.set_password('')
    login_page.click_on_submit_button()
    login_page.check_invalid_phone_message()
    login_page.check_invalid_password_message()
    error_message_phone  = login_page.check_invalid_phone_message()
    error_message_passw = login_page.check_invalid_password_message()
    assert error_message_phone.is_displayed(), "Message invalid phone is not visible"
    assert error_message_phone.text == 'Въведете валиден мобилен Мобилен телефон'

    assert error_message_passw.is_displayed(), "Message invalid password is not visible"
    assert error_message_passw.text == 'Моля въведете Вашата "Парола"'

# 26 test case ok
def logout(login_page):
    login_page.open_page()
    login_page.cookie_accept()
    login_page.click_on_phone_button()
    login_page.set_phone(const.LOGON_PHONE)
    login_page.set_password(const.PASSWORD)
    login_page.click_on_submit_button()
    login_page.click_on_logout_button()
    login_page.check_login_button_visible()
    login_button = login_page.check_login_button_visible()
    assert login_button.is_displayed(), "Button Login is not visible"
