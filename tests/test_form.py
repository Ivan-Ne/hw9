from selene import browser, have, command

from additional_package import resource


def test_fill_form(browser_personal_settings):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Neverov')
    browser.element('#userEmail').type('neverovsky@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8927654341')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1999"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(resource.path('1.jpg'))
    browser.element('#currentAddress').type('Saint-Petersburg')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()

    browser.element('[class="modal-content"]').should(have.text('Ivan Neverov'))
    browser.element('[class="modal-content"]').should(have.text('neverovsky@mail.ru'))
    browser.element('[class="modal-content"]').should(have.text('Male'))
    browser.element('[class="modal-content"]').should(have.text('8927654341'))
    browser.element('[class="modal-content"]').should(have.text('08 September,1999'))
    browser.element('[class="modal-content"]').should(have.text('Physics'))
    browser.element('[class="modal-content"]').should(have.text('Sports'))
    browser.element('[class="modal-content"]').should(have.text('1.jpg'))
    browser.element('[class="modal-content"]').should(have.text('Saint-Petersburg'))
    browser.element('[class="modal-content"]').should(have.text('NCR Delhi'))
