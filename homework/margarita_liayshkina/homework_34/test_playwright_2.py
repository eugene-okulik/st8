import pytest
from playwright.sync_api import Page, expect, BrowserContext, Playwright


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page


def test_colorchange_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    visible_after_button = page.locator("#visibleAfter")
    color_change_button = page.locator('#colorChange')
    expect(visible_after_button).to_be_visible()
    color_change_button.click()


def test_student_form(page):
    page.goto('https://demoqa.com/automation-practice-form')
    first_name = page.locator('#firstName')
    first_name.fill('Ivan')
    expect(first_name).to_have_value('Ivan')
    lastname = page.locator('#lastName')
    lastname.fill('Nikolaev')
    expect(lastname).to_have_value('Nikolaev')

    email = page.locator('#userEmail')
    email.fill('nikolasha333@gmail.com')
    expect(email).to_have_value('nikolasha333@gmail.com')

    gender = page.locator('//label[contains(text(), "Male")]')
    expect(gender).to_be_visible()
    gender.click()

    mobile = page.locator('#userNumber')
    mobile.fill('1234567890')
    expect(mobile).to_have_value('1234567890')

    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").select_option("4")
    page.locator(".react-datepicker__year-select").select_option("1995")
    page.locator(".react-datepicker__day--015").click()
    expect(page.locator("#dateOfBirthInput")).to_have_value("15 May 1995")

    subject_field = page.locator('#subjectsInput')
    subject_field.fill('Chemistry')
    subject_field.press("Enter")
    selected_subject = page.locator("//div[contains(@class, 'subjects-auto-complete__multi-value__label')]")
    expect(selected_subject).to_have_text("Chemistry")

    page.locator("label[for='hobbies-checkbox-2']").click()

    address_field = page.locator("#currentAddress")
    address_field.fill("123 Street-333")
    expect(address_field).to_have_value("123 Street-333")

    state_dropdown = page.locator('#state')
    state_dropdown.click()

    input_field_state = page.locator('#react-select-3-input')
    input_field_state.fill('NCR')
    input_field_state.press('Enter')
    expect(page.locator("#state .css-1uccc91-singleValue")).to_have_text("NCR")

    city_dropdown = page.locator('#city')
    city_dropdown.click()
    input_field_city = page.locator('#react-select-4-input')
    input_field_city.fill('Delhi')
    input_field_city.press('Enter')
    expect(page.locator("#city .css-1uccc91-singleValue")).to_have_text("Delhi")

    page.locator("#submit").click()

    modal = page.locator(".modal-content")
    expect(modal).to_be_visible()
