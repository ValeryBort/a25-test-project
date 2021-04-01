import pytest


testdata_correct = [
    ["gipoxor556@asfalio.com", "5Vx8LvGrno8p"],
    ["+71111111112", "5Vx8LvGrno8p"]
]


testdata_incorrect = [
    ["abc", "0"],
    ["", "5Vx8LvGrno8p"],
    ["gipoxor556@asfalio.com", ""],
    ["+71111111112", ""],
    ["", ""]
]


@pytest.mark.parametrize("login, password", testdata_correct)
def test_auth_correct_data(page, login, password):
    page.goto("https://dev.lk.tr-line.ru/sign-in")
    page.fill('input[name="login"]', login)
    page.fill('input[name="password"]', password)
    with page.expect_navigation(timeout=5000):
        page.click("text='Войти'")
    assert "application" in page.url


@pytest.mark.parametrize("login, password", testdata_incorrect)
def test_auth_incorrect_data(page, login, password):
    page.goto("https://dev.lk.tr-line.ru/sign-in")
    page.fill('input[name="login"]', login)
    page.fill('input[name="password"]', password)
    page.click("text='Войти'")
    popup_message = page.inner_text('div[role="status"] div div', timeout=3000)
    assert popup_message == "Неудачная попытка авторизоваться"


def test_auth_by_phone_number(page):
    page.goto("https://dev.lk.tr-line.ru/sign-in")
    page.fill('input[name="login"]', "+71111111112")
    visible = page.is_visible("text='Войти по SMS'")
    assert visible

