from additional_package.model.pages.registration_page import registration_page

def test_fill_form(browser_personal_settings):
    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_lastname('Neverov')
    registration_page.fill_email('neverovsky@mail.ru')
    registration_page.fill_gender()
    registration_page.fill_number('8927654341')
    registration_page.fill_birthdate(1999, 8, 8)
    registration_page.fill_subject('Physics')
    registration_page.choose_hobbies_checbox(1)
    registration_page.upload_picture('1.jpg')
    registration_page.fill_current_address('Saint-Petersburg')
    registration_page.choose_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit_registration()

    registration_page.assert_registered_info(
        'Ivan Neverov',
        'neverovsky@mail.ru',
        'Male',
        '8927654341',
        '08 September,1999',
        'Physics',
        'Sports',
        '1.jpg',
        'Saint-Petersburg',
        'NCR Delhi'
    )
