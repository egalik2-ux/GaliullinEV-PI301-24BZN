class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.name)
        additional = self.info()
        if additional:
            print(additional)


class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return 'Дата рождения: {}'.format(self.birthdate)

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return 'Описание: {}'.format(self.description)
