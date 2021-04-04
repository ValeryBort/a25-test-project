class SignInPage:
    def __init__(self, page, link):
        self.page = page
        self.link = link

    def open(self):
        self.page.goto(self.link)

    def fill_login(self, login):
        self.page.fill('input[name="login"]', login)

    def fill_password(self, password):
        self.page.fill('input[name="password"]', password)

    def sign_in(self):
        with self.page.expect_navigation(timeout=5000):
            self.page.click("text='Войти'")

    def sign_in_with_incorrect_data(self):
        self.page.click("text='Войти'")

    def assert_login_successful(self):
        assert "application" in self.page.url, 'Authentication failed'

    def assert_login_unsuccessful(self):
        popup_message = self.page.inner_text('div[role="status"] div div', timeout=3000)
        assert popup_message == "Неудачная попытка авторизоваться", 'There is no popup-message "Неудачная попытка авторизоваться"'

    def assert_sign_in_by_sms_button_visible(self):
        visible = self.page.is_visible("text='Войти по SMS'")
        assert visible, 'There is no new button "Войти по SMS"'

    def assert_sign_in_by_sms_button_invisible(self):
        visible = self.page.is_visible("text='Войти по SMS'")
        assert not visible, 'There is wrong button "Войти по SMS"'
