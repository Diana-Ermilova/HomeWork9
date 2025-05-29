from users_data.user_data import user
from test_page.test_reg_page import RegPage

def test_reg_page(configure_base_browser):
    registration_page = RegPage()
    registration_page.open().reg(user).check_user_registration(user)
