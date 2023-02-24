from Employee import Employee


class Developer(Employee):
    def __init__(self, name, salary_one_day, email, tech_stack):
        super().__init__(name, salary_one_day, email)
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
        return self.__class__(name=name, salary_one_day=salary_one_day, email='', tech_stack=tech_stack)

