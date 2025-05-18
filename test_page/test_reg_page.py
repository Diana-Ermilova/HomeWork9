import os

from users_data import user_data
from users_data.user_data import User
import conftest
from selene import browser, be, have
from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf8')


class RegPage():
    def  __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_phone = browser.element('#userNumber')
        self.date_picker = browser.element('.react-datepicker')
        self.date_of_birth_input = browser.element("#dateOfBirthInput")
        self.date_picker_year = self.date_picker.element('[class$="year-select"]')
        self.date_picker_month = self.date_picker.element('[class$="month-select"]')

    def set_first_name(self, first_name):
        self.first_name.type(first_name)
        return self

    def set_last_name(self, last_name):
        self.last_name.type(last_name)
        return self
    def set_user_email(self, user_email):
        self.user_email.type(user_email)
        return self

    def set_user_phone(self, user_phone):
        self.user_phone.type(user_phone)
        return self

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def set_gender(self, gender):
        genders = {
            "Male": '[for="gender-radio-1"]',
            "Female": '[for="gender-radio-2"]',
            "Other": '[for="gender-radio-3"]',
        }
        browser.element(genders[gender]).click()
        return self

    def set_birth_date(self, birth_date):
        self.date_of_birth_input.click()


        self.date_picker_month.click()
        self.date_picker_month.all('option').element_by(have.text(birth_date.strftime('%B'))).click()
        self.date_picker_year.click()
        self.date_picker_year.all('option').element_by(have.text(str(birth_date.year))).click()
        self.get_datepicker_day(birth_date.day).click()

        return self

    def get_datepicker_day(self, day):
        return self.date_picker.element(f'[class*="day--0{day}"]')

    def mobile_number(self, value):
        self.user_phone.type(value)
        return self

    def usr_address(self, value):
        browser.element('#currentAddress').type(value)
        return self
    def usr_address_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()
        return  self

    def usr_address_city(self, value):
        browser.element('#city').click().all('#city div').element_by(have.exact_text(value)).click()
        return  self

    def subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def hobbies(self, hobby):
        hobbies ={"Sports": '[for="hobbies-checkbox-1"]', "Reading": '[for="hobbies-checkbox-2"]', "Music": '[for="hobbies-checkbox-3"]'}
        for i in hobby.split(", "):
            browser.element(hobbies[i]).click()
        return self

    def upload_picture(self, img):
        file_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imgs', '20762.jpg')))
        browser.element('input[type="file"]').set_value(file_path)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def reg(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.email)
        self.user_phone.type(user.phone_number)
        self.set_gender(user.gender)
        self.set_birth_date(user.birth_date)
        self.usr_address(user.address)
        self.usr_address_state(user.state)
        self.usr_address_city(user.city)
        self.hobbies(user.hobbies)
        self.subjects(user.subjects)
        self.upload_picture(user.picture)
        self.submit()
        return self

    def check_user_registration(self, first_name, last_name, email, gender, phone_number, birth_date,
                                subjects, hobbies, picture, address, state, city):
        browser.element('.modal-content table').all('td:nth-child(2)').should(have.exact_texts(
            f'{first_name} {last_name}',
            email,
            gender,
            phone_number,
            birth_date.strftime('%d %B,%Y'),
            subjects,
            hobbies,
            picture,
            address,
            f'{state} {city}'
        )
    )


