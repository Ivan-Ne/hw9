from selene import browser, have, command
from additional_package import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').type(user.firstName)
        browser.element('#lastName').type(user.lastName)
        browser.element('#userEmail').type(user.userEmail)
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type(user.userNumber)
        if user.date <= 9:
            date = '00' + str(user.date)
        else:
            date = '0' + str(user.date)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{user.year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{user.month}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--{date}"]').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        browser.element(f'[for="hobbies-checkbox-{user.hobby}"]').click()
        browser.element('#uploadPicture').set_value(resource.path(user.fileName))
        browser.element('#currentAddress').type(user.currentAddress)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').click()

    def assert_registered_info(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(user.firstName + ' ' + user.lastName,
                                                                         user.userEmail,
                                                                         user.userGender,
                                                                         user.userNumber,
                                                                         '08 September,1999',
                                                                         user.subject,
                                                                         'Sports',
                                                                         user.fileName,
                                                                         user.currentAddress,
                                                                         user.state + ' ' + user.city
                                                                         ))


registration_page = RegistrationPage()
