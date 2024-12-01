def test_new_page(page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    click_button = page.locator("//a[@id='new-page-button']")
    with page.context.expect_page() as new_tab_info:
        click_button.click()  # Нажимаем кнопку, чтобы открыть новую вкладку
    new_tab_page = new_tab_info.value
    new_tab_page.wait_for_load_state()
    new_tab_text = new_tab_page.locator("//p[@id='result-text']").text_content()
    assert new_tab_text == "I am a new page in a new tab", "Текст на новой вкладке не совпадает с ожидаемым"
    page.bring_to_front()
    assert click_button.is_enabled(), "Кнопка 'Click' не активна на изначальной вкладке"
    page.close()
