from selenium.webdriver.common.devtools.v134.network import set_user_agent_override

from test_page.test_reg_page import RegPage
from datetime import date
from test_page import test_reg_page
import conftest

def test_fill_registration_form(configure_base_browser):
    RegPage()\
        .open()\
        .set_gender('Other')\
        .set_first_name('Diana')\
        .set_last_name('Ermilova')\
        .set_user_email('testmail.01@gmail.com')\
        .set_user_phone('8800123121')\
        .set_birth_date(date.fromisoformat('1996-09-18'))\
        .usr_address('London, county of Surrey, Privet Drive 4')\
        .usr_address_state('Haryana')\
        .usr_address_city('Panipat')\
        .subjects('Physics')\
        .hobbies('Sports')\
        .upload_picture('20762.jpg')\
        .submit()\
        .check_user_registration(
        'Diana',
        'Ermilova',
        'testmail.01@gmail.com',
        'Other',
        '8800123121',
        date.fromisoformat('1996-09-18'),
        'Physics',
        'Sports',
        '20762.jpg',
        'London, county of Surrey, Privet Drive 4',
        'Haryana',
        'Panipat'
    )


