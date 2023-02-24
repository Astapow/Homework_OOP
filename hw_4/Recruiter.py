from Employee import Employee


class Recruiter(Employee):
    def work(self):
        return f'{super().work()[:-1]} and start hiring.'
