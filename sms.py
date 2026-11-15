class Person:
    def __init__(self, name, patronymic, surname, phones):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private')

    def get_work_phone(self):
        return self.phones.get('work')

    def get_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_sms_text(self):
        return (f'Уважаемый {self.name} {self.patronymic}! '
                f'Примите участие в нашем беспроигрышном конкурсе '
                f'для физических лиц.')


class Company:
    def __init__(self, name, type_, phones, *employees):
        self.name = name
        self.type_ = type_
        self.phones = phones
        self.employees = employees

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for employee in self.employees:
            if employee.get_work_phone() is not None:
                return employee.get_work_phone()
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return (f'Для компании {self.name} есть супер предложение! '
                f'Примите участие в нашем беспроигрышном конкурсе '
                f'для {self.type_}.')


def send_sms(*objects):
    for obj in objects:
        phone = obj.get_phone()
        if phone is not None:
            print(f'Отправлено СМС на номер {phone} с текстом: {obj.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {obj.get_name()}')
