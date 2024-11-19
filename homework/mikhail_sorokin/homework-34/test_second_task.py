from playwright.sync_api import sync_playwright


def test_form_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demoqa.com/automation-practice-form')

        first_name = page.locator("#firstName")
        last_name = page.locator("#lastName")
        email = page.locator("#userEmail")
        gender_male = page.locator("label[for='gender-radio-1']")
        mobile_number = page.locator("#userNumber")
        subjects_input = page.locator("#subjectsInput")
        hobby_music = page.locator("label[for='hobbies-checkbox-3']")
        current_address = page.locator("#currentAddress")
        state_dropdown = page.locator("#state")
        state_selection = page.locator("div[id*='react-select-3-option-0']")
        city_dropdown = page.locator("#city")
        city_selection = page.locator("div[id*='react-select-4-option-0']")
        submit_button = page.locator("//button[@id='submit']")

        # Заполнение формы
        first_name.fill("test")
        last_name.fill("test")
        email.fill("test@mail.com")
        gender_male.click()
        mobile_number.fill('7995232331')

        subjects_input.fill('Maths')
        subjects_input.press("Enter")
        page.wait_for_timeout(500)

        hobby_music.click()

        current_address.fill('tests')

        state_dropdown.click()
        page.wait_for_selector("div[id*='react-select-3-option-0']")
        state_selection.click()
        page.wait_for_timeout(500)

        city_dropdown.click()
        page.wait_for_selector("div[id*='react-select-4-option-0']")
        city_selection.click()

        page.wait_for_timeout(1000)

        submit_button.wait_for(state="attached")
        submit_button.click()

        browser.close()
