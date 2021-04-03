import pytest

from page_objects.restore_password_page import RestorePasswordPage

link = "https://dev.lk.tr-line.ru/restore-password"

email_not_registered = ["qwerty@mail.ru"]
email_incorrect = [
    "@.ru",
    ".",
    "1234567890",
    "Qwerty",
    "Йцукен",
]


@pytest.mark.parametrize("email", email_not_registered)
def test_restore_password_with_not_registered_email(page, email):
    """
    Тест-кейс 3.2
    """
    res_pass_page = RestorePasswordPage(page, link)
    res_pass_page.open()
    res_pass_page.fill_email(email)
    res_pass_page.click_reset_password()
    res_pass_page.assert_popup_message_unsuccessful_restore()


def test_restore_password_with_empty_field(page):
    """
    Тест-кейс 3.3
    """
    res_pass_page = RestorePasswordPage(page, link)
    res_pass_page.open()
    res_pass_page.click_reset_password()
    res_pass_page.assert_popup_message_unsuccessful_restore()


@pytest.mark.parametrize("email", email_incorrect)
def test_restore_password_with_incorrect_email(page, email):
    """
    Тест-кейс 3.4
    """
    res_pass_page = RestorePasswordPage(page, link)
    res_pass_page.open()
    res_pass_page.fill_email(email)
    res_pass_page.assert_message_incorrect_email()
