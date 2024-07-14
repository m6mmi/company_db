from random import choice, randint

from model import Base, Employee, Gender, Department, Salary
from session import session
from faker import Faker


def create_employees(n=100):
    faker = Faker()
    genders = [Gender.M, Gender.F]
    employee = [
        Employee(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=faker.date_of_birth(minimum_age=18, maximum_age=65),
            hire_date=faker.date_of_birth(minimum_age=0, maximum_age=10),
            gender=faker.random_element(elements=genders)
        )
        for _ in range(n)
    ]
    session.add_all(employee)
    session.commit()


def create_departments():
    departments = []


def assign_employees_to_departments():
    employees = session.query(Employee).all()
    departments = session.query(Department).all()
    for employee in employees:
        employee.department.append(
            choice(departments)
        )


def salaries():
    faker = Faker()
    employees = session.query(Employee).all()
    for employee in employees:
        salary = randint(30_000, 150_000)
        employee.salaries.append(
            Salary(
                amount=salary,
                date=faker.date_time(),
                employee_id=employee
            )
        )
    session.commit()


def main():
    Base.metadata.create_all(session.bind)

    # print('Generating employees ...')
    # create_employees()
    # print('Generating departments ...')
    # create_departments()
    # print('Assigning employees ...')
    # assign_employees_to_departments()
    print('Creating salaries ...')
    salaries()


if __name__ == '__main__':
    main()
