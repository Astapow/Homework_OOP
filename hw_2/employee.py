class Employee:
    def __init__(self, name, salary_one_day):
        self.name = name
        self.salary_one_day = salary_one_day

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

    def check_salary(self, days):
        return self.salary_one_day * days


class Recruiter(Employee):
    def work(self):
        return f'{super().work()[:-1]} and start hiring.'


class Developer(Employee):
    def __init__(self, name, salary_one_day, tech_stack):
        super().__init__(name, salary_one_day)
        self.tech_stack = tech_stack

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def work(self):
        return f'{super().work()[:-1]} and start coding.'

    def __add__(self, other):
        name = self.name + ' ' + other.name
        salary_one_day = max(self.salary_one_day, other.salary_one_day)
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        return self.__class__(name=name, salary_one_day=salary_one_day, tech_stack=tech_stack)


if __name__ == '__main__':
    elvis = Developer('elvis', 100, [])
    print(elvis.work())

    recruiter = Recruiter('mark', 75)
    print(recruiter.work())

    will_em = Employee('will', 65)
    jane_em = Employee('jane', 85)
    print(will_em > jane_em)
    print(will_em < jane_em)

    michael = Employee('michael', 95).check_salary(10)
    print(michael)

    oliver = Developer('oliver', 70, ('css', 'c+', 'python'))
    claus = Developer('claus', 85, ('js', 'java'))
    print(claus > oliver)
    print(claus + oliver)
