from additional_package.model.pages.registration_page import registration_page
from additional_package.data.users import User


def test_fill_form(browser_personal_settings):
    ivan = User(firstName='Ivan', lastName='Neverov',
                userEmail='neverovsky@mail.ru', userGender='Male', userNumber='8927654341',
                year=1999, month=8, date=8, subject='Physics', hobby=1,
                fileName='1.jpg', currentAddress='Saint-Petersburg', state='NCR', city='Delhi')
    registration_page.open()
    registration_page.register(ivan)
    registration_page.assert_registered_info(ivan)
