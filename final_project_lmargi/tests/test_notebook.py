import time

from final_project_lmargi.tests.conftest import card_page

# 2 test OK
def car_save_notebook(login_page, notebook_page, card_page):
    login_page.make_login()

    checked_car_url = '19014658/vw-polo-cross'
    card_page.open_card(checked_car_url)
    card_page.save_car_ad_notebook()

    notebook_page.open_page()
    notebook_links = notebook_page.get_car_links()
    notebook_page.clean_notebook()
    assert checked_car_url in notebook_links, f"Error: {checked_car_url} не входит в записной книжке!"

# 3 test OK
def car_remove_notebook(login_page, notebook_page, card_page):
    login_page.make_login()

    checked_car_url = '19014658/vw-polo-cross'
    card_page.open_card(checked_car_url)
    time.sleep(1)
    card_page.save_car_ad_notebook()
    time.sleep(1)
    card_page.remove_car_from_notebook()
    notebook_page.open_page()
    notebook_links = notebook_page.get_car_links()
    assert checked_car_url not in notebook_links, f"Error: {checked_car_url} все еще входит в записной книжке!"

