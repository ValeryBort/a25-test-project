DEFAULT_TIMEOUT = 3000


class RestorePasswordPage:
    def __init__(self, page, link):
        self.page = page
        self.link = link

    def open(self):
        self.page.goto(self.link)

    def click_reset_password(self):
        self.page.click("text='Сбросить пароль'")

    def assert_popup_message_unsuccessful_restore(self):
        popup_message = self.page.inner_text("div[role=status] div div", timeout=DEFAULT_TIMEOUT)
        assert popup_message == "Пользователя с такими данными не существует.", 'There is no correct popup-message'

    def assert_message_incorrect_email(self):
        message = self.page.inner_text("div[role=alert] div div", timeout=DEFAULT_TIMEOUT)
        assert message == "Введен некорректный e-mail", 'There is no message, that email is incorrect'

    def fill_email(self, email):
        self.page.fill('input[name="forget_email"]', email)
