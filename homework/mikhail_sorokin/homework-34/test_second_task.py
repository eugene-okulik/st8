import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page


def test_form_selectors(page):
    page.goto('https://demoqa.com/automation-practice-form')

    first_name = page.locator("#firstName")  # Имя
    last_name = page.locator("#lastName")  # Фамилия
    email = page.locator("#userEmail")  # Email
    gender_male = page.locator("label[for='gender-radio-1']")  # Мужчина
    mobile_number = page.locator("#userNumber")
    subjects_input = page.locator("#subjectsInput")
    hobby_music = page.locator("label[for='hobbies-checkbox-3']")  # Музыка
    current_address = page.locator("#currentAddress")
    state_dropdown = page.locator("#state")
    state_selection = page.locator("div[id*='react-select-3-option-0']")  # Выбор штата NCR
    city_dropdown = page.locator("#city")
    city_selection = page.locator("div[id*='react-select-4-option-0']")  # Выбор города Gurgaon
    submit_button = page.locator("//button[@id='submit']")

    first_name.fill("test")
    last_name.fill("test")
    email.fill("test@mail.com")
    gender_male.click()
    mobile_number.fill('7995232331')

    subjects_input.fill('Maths')
    subjects_input.press("Enter")

    hobby_music.click()

    current_address.fill('tests')

    state_dropdown.click()
    page.wait_for_selector("div[id*='react-select-3-option-0']")
    state_selection.click()

    city_dropdown.click()
    page.wait_for_selector("div[id*='react-select-4-option-0']")
    city_selection.click()

    submit_button.click()
