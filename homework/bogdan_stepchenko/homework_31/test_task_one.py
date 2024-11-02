from functions_for_task_one import opening_product_in_new_tab, find_product_card_and_get_name_and_price, \
    find_product_and_get_name_and_price, find_add_to_cart_button_and_click, wait_for_alert_and_accept, \
    close_active_tab_and_switch_to_another, find_cart_button_and_click, find_product_in_cart_and_get_name_and_price


def test_add_product_to_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')

    product_card, card_name, card_price = find_product_card_and_get_name_and_price(driver)
    opening_product_in_new_tab(driver, product_card)
    product_content, product_name, product_price = find_product_and_get_name_and_price(driver)

    assert card_name == product_name, 'Product Name on screen is different from Product Name on card!'
    assert card_price == product_price, 'Product Price on screen is different from Product Price on card!'

    find_add_to_cart_button_and_click(product_content)
    wait_for_alert_and_accept(driver)
    close_active_tab_and_switch_to_another(driver)
    find_cart_button_and_click(driver)
    product_name_in_cart, product_price_in_cart = find_product_in_cart_and_get_name_and_price(driver)

    assert product_name == product_name_in_cart, 'Product Name in cart is different from Product Name on card!'
    assert product_price == '$' + product_price_in_cart, 'Product Price in cart is different from Product Name on card!'
