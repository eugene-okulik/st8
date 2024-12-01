def handle_dialog_accept(dialog):
    print(f"Диалог открыт: {dialog.message}")
    dialog.accept()


def test_alert_click(page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", handle_dialog_accept)
    confirm_button = page.locator("a:has-text('Click')")
    confirm_button.click()
    result_block = page.locator("//p[@id='result-text']").text_content()
    assert result_block == "Ok"
    page.close()
