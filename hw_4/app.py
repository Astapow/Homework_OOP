import datetime
import traceback

from Employee import Employee
from Developer import Developer
from Recruiter import Recruiter


def main():
    recruiter = Recruiter('mark', 70, 'mark@gmail.com')
    will_em = Employee('will', 65, 'will@gmail.com')
    jane_em = Employee('jane', 85, 'jane@gmail.com')
    oliver = Developer('oliver', 70, 'oliver@gmail.com', ('css', 'c+', 'python'))
    claus = Developer('claus', 85, 'claus@gmail.com', ('js', 'java'))
    wekkend = Developer('oliver', 70, 'olliver@gmail.com', ('css', 'c+', 'python')).check_salary()

    print(recruiter.work())

    print(will_em > jane_em)
    print(will_em < jane_em)

    print(claus > oliver)
    print(claus + oliver)

    print(wekkend)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        with open("logs.txt", "a") as file:
            now = datetime.datetime.now()
            traceback_message = traceback.format_exc()
            file.write(f'{now}:{traceback_message}')
