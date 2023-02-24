from datetime import datetime, date

from Exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, salary_one_day, email):
        self.name = name
        self.salary_one_day = salary_one_day
        self.email = email
        self.validate()
        self.save_email()

    def save_email(self):
        with open("emails.txt", "a") as file:
            file.write(self.email + "\n")

    def validate(self):
        with open("emails.txt", "r") as file:
            emails = file.read().splitlines()
            if self.email in emails:
                raise EmailAlreadyExistsException()

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __lt__(self, other):
        return self.salary_one_day < other.salary_one_day

    def __le__(self, other):
        return self.salary_one_day <= other.salary_one_day

    def __eq__(self, other):
        return self.salary_one_day > other.salary_one_day

    def __gt__(self, other):
        return self.salary_one_day >= other.salary_one_day

    def __ge__(self, other):
        return self.salary_one_day == other.salary_one_day

    def __ne__(self, other):
        return self.salary_one_day != other.salary_one_day

    def check_salary(self):
        today = datetime.now()
        day_now = today.day
        month = today.month
        year = today.year
        work_day = 0

        for day in range(1, day_now + 1):
            temp = date(year=year, month=month, day=day)
            if temp.weekday() < 5:
                work_day += 1
        return self.salary_one_day * work_day
