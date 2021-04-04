import pytest
from page_objects.sign_up_page import SignUpPage

link = "https://dev.lk.tr-line.ru/sign-up"

testdata_email_phone = [
    ["midihe8534@tlhao86.com", "5555555555"],
    ["qwerty@mail.ru", "1111111112"]
]

testdata_lname_fname = [
    ['-', '-'],
    ['@', '@'],
    ['0', '0'],
    [' ', ' '],
]


@pytest.mark.parametrize("email, phone", testdata_email_phone)
def test_sign_up_already_registered_email_or_phone(page, email, phone):
    """
    Тест-кейс 1.2, 1.3
    """
    sign_up = SignUpPage(page, link)
    sign_up.open()
    sign_up.fill_email(email)
    sign_up.fill_phone_number(phone)
    sign_up.click_next_button()
    sign_up.assert_error_message_email_phone_already_registered()
    sign_up.click_go_to_sign_in_button()
    sign_up.assert_redirect_to_sign_in_page_successful()


def test_sign_up_with_empty_email_and_phone(page):
    """
    Тест-кейс 1.4
    """
    sign_up = SignUpPage(page, link)
    sign_up.open()
    sign_up.click_next_button()
    sign_up.assert_error_message_should_set_email()
    sign_up.assert_error_message_should_set_phone()


def test_sign_up_incorrect_promocode(page):
    """
    Тест-кейс 1.5
    """
    sign_up = SignUpPage(page, link)
    sign_up.open()
    sign_up.fill_email("1234567890@ya.ru")
    sign_up.fill_phone_number("+70876543219")
    sign_up.fill_promocode("Йцукен")
    sign_up.click_next_button()
    sign_up.assert_error_message_incorrect_promocode()


def test_sign_up_with_empty_fname_lname(page):
    """
    Тест-кейс 1.6
    """
    sign_up = SignUpPage(page, link)
    sign_up.open()
    sign_up.fill_email("1234567890@ya.ru")
    sign_up.fill_phone_number("+70876543219")
    sign_up.click_next_button()
    sign_up.click_sign_up_button()
    sign_up.assert_error_message_set_last_name()
    sign_up.assert_error_message_set_first_name()


# @pytest.mark.parametrize("lname, fname", testdata_lname_fname)
# def test_sign_up_with_spec_char_instead_of_fname_lname(page, lname, fname):
#     """
#     Тест-кейс 1.7, 1.8
#     """
#     sign_up = SignUpPage(page, link)
#     sign_up.open()
#     sign_up.fill_email("1234567890@ya.ru")
#     sign_up.fill_phone_number("+70876543219")
#     sign_up.click_next_button()
#     sign_up.fill_last_name(lname)
#     sign_up.fill_first_name(fname)
#     sign_up.assert_error_message_set_last_name()








