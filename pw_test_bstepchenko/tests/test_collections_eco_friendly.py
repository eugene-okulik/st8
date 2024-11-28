def test_displaying_all_product_cards(pw_eco_friendly):
    pw_eco_friendly.open_by_url()
    pw_eco_friendly.check_that_number_of_displayed_products_in_counter_is(12)
    pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(12)
    pw_eco_friendly.open_selector_and_choose_24()
    pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(18)


def test_workability_of_products_list_view(pw_eco_friendly):
    pw_eco_friendly.open_by_url()
    pw_eco_friendly.change_products_view_to_list()
    pw_eco_friendly.check_that_number_of_displayed_products_in_counter_is(10)
    pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(10)


def test_select_products_with_white_color_only(pw_eco_friendly):
    pw_eco_friendly.open_by_url()
    pw_eco_friendly.open_color_dropdown_and_select_white_color()
    pw_eco_friendly.check_that_all_products_has_white_color()
    pw_eco_friendly.check_counter_has_correct_value_of_founded_cards()
