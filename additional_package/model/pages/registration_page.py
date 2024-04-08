from selene import browser, have, command
from additional_package import resource

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_lastname(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_birthdate(self, year=9, month=8, date=8):
        if date <= 9:
            date = '00' + str(date)
        else:
            date = '0' + str(date)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{month}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--{date}"]').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)

    def choose_hobbies_checbox(self, value=1):
        browser.element(f'[for="hobbies-checkbox-{value}"]').click()

    def upload_picture(self, name):
        browser.element('#uploadPicture').set_value(resource.path(name))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value='NCR'):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value='Delhi'):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit_registration(self):
        browser.element('#submit').click()

    def assert_registered_info(self, name, email, sex, number, birthday, subject, hobby, file_name, address,
                               state_and_city):
        browser.element('.table').all('td').even.should(have.exact_texts(name,
                                                                         email,
                                                                         sex,
                                                                         number,
                                                                         birthday,
                                                                         subject,
                                                                         hobby,
                                                                         file_name,
                                                                         address,
                                                                         state_and_city
                                                                         ))

registration_page = RegistrationPage()