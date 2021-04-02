import pytest

from page_objects.sign_in import SignInPage

link = "https://dev.lk.tr-line.ru/sign-in"

testdata_correct = [
    ["gipoxor556@asfalio.com", "5Vx8LvGrno8p"],
    ["+71111111112", "5Vx8LvGrno8p"],
]

testdata_incorrect = [
    ["abc", "0"],
    ["", "5Vx8LvGrno8p"],
    ["gipoxor556@asfalio.com", ""],
    ["+71111111112", ""],
    ["", ""],
]

testdata_phone_number = [
    '+71111111112',
    '89876543210',
    '0',
    '9',
    '+',
    '(',
]

testdata_incorrect_phone_number = [
    '@',
    '.',
]


@pytest.mark.parametrize("login, password", testdata_correct)
def test_auth_correct_data(page, login, password):
    sign_in_page = SignInPage(page, link)
    sign_in_page.open()
    sign_in_page.fill_login(login)
    sign_in_page.fill_password(password)
    sign_in_page.sign_in()
    sign_in_page.assert_login_successful()


@pytest.mark.parametrize("login, password", testdata_incorrect)
def test_auth_incorrect_data(page, login, password):
    sign_in_page = SignInPage(page, link)
    sign_in_page.open()
    sign_in_page.fill_login(login)
    sign_in_page.fill_password(password)
    sign_in_page.sign_in_with_incorrect_data()
    sign_in_page.assert_login_unsuccessful()


@pytest.mark.parametrize("login", testdata_phone_number)
def test_auth_by_phone_number(page, login):
    sign_in_page = SignInPage(page, link)
    sign_in_page.open()
    sign_in_page.fill_login(login)
    sign_in_page.assert_sign_in_by_sms_button_visible()


@pytest.mark.parametrize("login", testdata_incorrect_phone_number)
def test_sign_in_by_sms_button_invisible(page, login):
    sign_in_page = SignInPage(page, link)
    sign_in_page.open()
    sign_in_page.fill_login(login)
    sign_in_page.assert_sign_in_by_sms_button_invisible()


