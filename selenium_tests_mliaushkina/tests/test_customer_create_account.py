import random
import string


def test_create_account_ok(customer_create_page):
    customer_create_page.open_page()
    customer_create_page.set_first_name('margarita')
    customer_create_page.set_second_name('liaushkina')

    my_email_random = ''.join(random.choices(string.ascii_letters, k=4))
    my_email = 'liaushkina' + my_email_random + '@ya.ru'

    customer_create_page.set_email(my_email)
    customer_create_page.set_password('Margarita123')
    customer_create_page.set_confirm_password('Margarita123')
    customer_create_page.click_on_create_button()
    customer_create_page.check_if_success_message_visible()


def test_format_email_invalid(customer_create_page):
    customer_create_page.open_page()
    customer_create_page.set_email('////////???')
    customer_create_page.click_on_create_button()
    customer_create_page.check_if_email_error_visible()


def test_confirm_password_error_message(customer_create_page):
    customer_create_page.open_page()
    customer_create_page.set_password('Margarita123')
    customer_create_page.set_confirm_password('Margarita124')
    customer_create_page.click_on_create_button()
    customer_create_page.check_if_confirm_password_error_visible()
