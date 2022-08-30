from random import randint, choice
from string import ascii_letters


class CredentialGenerator:
    name = 'iisaeva'
    thread = 2
    domain = '@yandex.ru'

    def random_email(self):
        return ''.join([self.name, str(self.thread), str(randint(100, 999)), self.domain])

    def random_password(self):
        random_string = ''.join([choice(ascii_letters) for _ in range(0,randint(3, 9))])
        random_number = str(self.thread*randint(100,499) + 1)
        return ''.join([random_number, random_string])


cls = CredentialGenerator()
print(cls.random_email())
print(cls.random_password())
