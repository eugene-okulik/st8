import  allure
from final_project_lmargi.tests.conftest import card_page
from final_project_lmargi.pages.const import const_notebook as const


@allure.feature('notebook functionality')
@allure.story('Check save the car in a notebook')
@allure.title('Проверка сохранения объявления в записной книжке')
def test_car_save_notebook(login_page, adlist_page, notebook_page, card_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_first_card()
    card_page.save_card_ad_notebook()
    checked_car_url = card_page.get_current_relative_url()
    notebook_page.open_page()
    notebook_links = notebook_page.get_car_links()
    assert checked_car_url in notebook_links, f"Error: {checked_car_url} not added to notebook "
    notebook_page.clean_notebook()


@allure.feature('notebook functionality')
@allure.story('Check delete the car from notebook')
@allure.title('Проверка удаления объявления из записной книжки')
def test_car_remove_notebook(login_page, adlist_page, notebook_page, card_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_first_card()
    card_page.save_card_ad_notebook()
    checked_car_url = card_page.get_current_relative_url()
    notebook_page.open_page()
    notebook_links = notebook_page.get_car_links()
    notebook_page.clean_notebook()
    notebook_page.open_page()
    expected_message = notebook_page.get_empty_message_text(const.MESSAGE_DELETE_NOTEBOOK)
    actual_message = const.MESSAGE_DELETE_NOTEBOOK
    assert  expected_message == actual_message, "Message not displayed"
    assert checked_car_url in notebook_links, f"Error: {checked_car_url} not removed from notebook"
