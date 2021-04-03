DEFAULT_TIMEOUT = 5000


class SignUpPage:
    def __init__(self, page, link):
        self.page = page
        self.link = link

    def open(self):
        self.page.goto(self.link)

    def fill_email(self, email):
        self.page.fill('input[name="e-mail"]', email)

    def fill_phone_number(self, phone):
        self.page.click('input[name="phone"]')
        for n in phone:
            self.page.keyboard.type(n)

    def fill_promocode(self, promocode):
        self.page.fill('input[name="promocode"]', promocode)

    def fill_last_name(self, lname):
        self.page.fill('input[name="lname"]', lname)

    def fill_first_name(self, fname):
        self.page.fill('input[name="fname"]', fname)

    def fill_father_name(self, father_name):
        self.page.fill('input[name="father_name"]', father_name)

    def click_sign_up_button(self):
        self.page.click("text='Зарегистрироваться'")

    def click_next_button(self):
        self.page.click("text='Далее'")

    def click_back_button(self):
        with self.page.expect_navigation(timeout=DEFAULT_TIMEOUT):
            self.page.click("text='Назад'")

    def click_go_to_sign_in_button(self):
        with self.page.expect_navigation(timeout=DEFAULT_TIMEOUT):
            self.page.click("text='Перейти к авторизации'")

    def assert_error_message_email_phone_already_registered(self):
        visible = self.page.is_visible('div[role=status] div div')
        assert (visible,
                'There is no error message "Пользователь с указанным e-mail/телефоном уже зарегистрирован"')

    def assert_redirect_to_sign_in_page_successful(self):
        assert "sign-in" in self.page.url, 'There is no redirect to sign-in page'

    def assert_error_message_should_set_email(self):
        visible = self.page.is_visible("text='Необходимо указать e-mail'")
        assert visible, 'There is no error message "Необходимо указать e-mail"'

    def assert_error_message_should_set_phone(self):
        visible = self.page.is_visible("text='Необходимо указать телефон'")
        assert visible, 'There is no error message "Необходимо указать телефон"'

    def assert_error_message_incorrect_promocode(self):
        visible = self.page.is_visible('form .v-input:nth-child(3) .v-messages__message', timeout=DEFAULT_TIMEOUT)
        assert visible, 'There is no error message "Такого промокода не существует"'

    def assert_error_message_set_last_name(self):
        text = self.page.inner_text(".v-window-item--active form div.v-input:nth-child(1) .v-messages__message",
                                    timeout=DEFAULT_TIMEOUT)
        assert text == 'Поле обязательно для заполнения', 'There is no error message "Поле обязательно для заполнения"'

    def assert_error_message_set_first_name(self):
        text = self.page.inner_text(".v-window-item--active form div.v-input:nth-child(2) .v-messages__message",
                                    timeout=DEFAULT_TIMEOUT)
        assert text == 'Поле обязательно для заполнения', 'There is no error message "Поле обязательно для заполнения"'






