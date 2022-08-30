import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from CredentialGenerator import CredentialGenerator
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as expected


class PersonalAccount:
    url = 'https://stellarburgers.nomoreparties.site/'
    user_name = 'Iuliia'
    email = ''
    correct_password = ''
    timeout = 10
    driver = None

    @classmethod
    def setup_class(cls):
        cred_generator = CredentialGenerator()
        cls.email = cred_generator.random_email()
        cls.correct_password = cred_generator.random_password()
        cls.driver = webdriver.Chrome()
        cls.wait = Wait(cls.driver, cls.timeout)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_go_to_personal_account_not_authorized_user(self):

        self.driver.get(self.url)
        self.driver.maximize_window()

        