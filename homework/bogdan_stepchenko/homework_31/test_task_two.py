from functions_for_task_two import wait_for_1st_product_and_get_name, \
    hover_on_card_and_click_compare_button, find_compare_count_and_product_name


def test_add_item_to_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    first_product, product_name_element = wait_for_1st_product_and_get_name(driver)
    hover_on_card_and_click_compare_button(driver, first_product)

    compare_count, compare_item_name = find_compare_count_and_product_name(driver)
    assert '1 item' == compare_count, 'Count of comparing products is incorrect!'
    assert product_name_element == compare_item_name, 'Product name in comparing is incorrect!'
