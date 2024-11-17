from playwright.sync_api import Page
import random


class RegistrationsForm:
    BASE_URL = 'https://demoqa.com/automation-practice-form'

    def __init__(self, page: Page, base_url=BASE_URL):
        self.base_url = base_url
        self.page = page

    def open_web_page(self):
        self.page.goto(self.base_url)

    def fill_first_name(self, name):
        first_name_field = self.page.get_by_role('textbox', name='First Name')
        first_name_field.fill(name)

    def fill_last_name(self, last_name):
        last_name_field = self.page.get_by_role('textbox', name='Last Name')
        last_name_field.fill(last_name)

    def fill_email_field(self, email):
        email_field = self.page.get_by_role('textbox', name='name@example.com')
        email_field.fill(email)

    def select_random_gender(self):
        genders = [
            'label[for="gender-radio-1"]',
            'label[for="gender-radio-2"]',
            'label[for="gender-radio-3"]'
        ]
        gender = self.page.locator(random.choice(genders))
        gender.click()

    def fill_phone_field(self, phone):
        phone_field = self.page.get_by_role('textbox', name='Mobile Number')
        phone_field.fill(phone)

    def select_random_date(self):
        date_field = self.page.locator('#dateOfBirthInput')
        date_field.click()

        random_year = random.randint(1950, 2024)
        random_month = random.randint(0, 11)
        random_day = random.randint(1, 29)

        month_select = self.page.locator('.react-datepicker__month-select')
        month_select.select_option(value=str(random_month))

        year_select = self.page.locator('.react-datepicker__year-select')
        year_select.select_option(value=str(random_year))

        day_element = self.page.locator(f"div.react-datepicker__month "
                                        f"div.react-datepicker__day:has-text('{random_day}')")
        day_element.nth(0).click()

    def select_subject(self, subject):
        subject_field = self.page.locator('#subjectsInput')
        subject_field.fill(subject)
        self.page.wait_for_selector('.subjects-auto-complete__value-container', timeout=5000)
        subject_field.press('Enter')

    def select_random_hobbies(self):
        hobbies = [
            'label[for="hobbies-checkbox-1"]',
            'label[for="hobbies-checkbox-2"]',
            'label[for="hobbies-checkbox-3"]'
        ]
        selected_hobbies = self.page.locator(random.choice(hobbies))
        selected_hobbies.click()

    def fill_address_field(self, address):
        address_field = self.page.get_by_role('textbox', name='Current Address')
        address_field.fill(address)

    def select_state(self, state):
        state_container = self.page.locator('#state')
        state_container.click()
        state_field = self.page.locator('#react-select-3-input')
        state_field.fill(state)
        state_field.press('Enter')

    def select_city(self, city):
        city_container = self.page.locator('#city')
        city_container.click()
        city_field = self.page.locator('#react-select-4-input')
        city_field.fill(city)
        city_field.press('Enter')

    def fill_all_registration_fields(self, expected_first_name, expected_last_name,
                                     expected_email, expected_subject, expected_phone,
                                     expected_address, expected_state, expected_city):
        self.fill_first_name(expected_first_name)
        self.fill_last_name(expected_last_name)
        self.fill_email_field(expected_email)
        self.select_random_gender()
        self.fill_phone_field(expected_phone)
        self.select_random_date()
        self.select_subject(expected_subject)
        self.select_random_hobbies()
        self.fill_address_field(expected_address)
        self.select_state(expected_state)
        self.select_city(expected_city)

    def click_submit_button(self):
        submit_button = self.page.get_by_role('button')
        submit_button.click()

    def check_user_data_in_result_table(self, expected_first_name, expected_last_name,
                                        expected_email, expected_subject, expected_phone,
                                        expected_address, expected_state, expected_city):
        expected_values = {
            "Student Name": f"{expected_first_name} {expected_last_name}",
            "Student Email": expected_email,
            "Mobile": expected_phone,
            "Subjects": expected_subject,
            "Address": expected_address,
            "State and City": f'{expected_state} {expected_city}'
        }

        rows = self.page.locator('table.table tbody tr')

        for i in range(rows.count()):
            name_element = rows.nth(i).locator("td:nth-child(1)")
            value_element = rows.nth(i).locator("td:nth-child(2)")

            name_text = name_element.text_content().strip()
            value_text = value_element.text_content().strip()

            if name_element in expected_values.keys():
                assert value_text == expected_values[name_text], 'Value in table is not correct!'
