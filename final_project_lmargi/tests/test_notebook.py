import  allure
from final_project_lmargi.tests.conftest import card_page


@allure.feature('notebook functionality')
@allure.story('Check save the car in a notebook')
@allure.title('Проверка сохранения объявления в записной книжке')
def car_save_notebook(login_page, adlist_page, notebook_page, card_page):
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
def car_remove_notebook(login_page, adlist_page, notebook_page, card_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_first_card()
    card_page.save_card_ad_notebook()
    checked_car_url = card_page.get_current_relative_url()
    notebook_page.open_page()
    notebook_links = notebook_page.get_car_links()
    notebook_page.clean_notebook()
    notebook_links = notebook_page.get_car_links()
    empty_text = notebook_page.get_empty_message_text()
    assert empty_text == "Няма записани обяви във вашият профил!", f"Error:"

    assert checked_car_url not in notebook_links, f"Error: {checked_car_url} not removed from notebook"
