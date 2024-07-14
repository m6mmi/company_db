import datetime
import random

from faker import Faker

from model import Base, Employee, Gender, Department, Salary
from session import session


def create_employees(session, n=100):
    faker = Faker()
    genders = [Gender.M, Gender.F]
    employees = [
        Employee(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=faker.date_of_birth(),
            hire_date=faker.date_of_birth(),
            gender=faker.random_element(elements=genders),
        )
        for _ in range(n)
    ]
    session.add_all(employees)
    session.commit()


def create_departments(session):
    departments = [
        "Human Resources",
        "Finance",
        "Marketing",
        "Sales",
        "Information Technology",
        "Operations",
        "Customer Service",
        "Legal",
        "Research and Development",
        "Procurement",
        "Corporate Strategy",
        "Corporate Communications",
        "Quality Assurance",
        "Risk Management",
        "Training and Development",
    ]
    session.add_all([
        Department(name=name)
        for name in departments
    ])
    session.commit()


def assign_employees_to_departments(session):
    employees = session.query(Employee)
    departments = session.query(Department).all()
    for employee in employees:
        employee.departments.append(
            random.choice(departments)
        )
    session.commit()


def create_salaries(session):
    employees = session.query(Employee)
    for employee in employees:
        salary = random.randint(30_000, 150_000)
        employee.salaries.append(
            Salary(
                amount=salary,
                date=datetime.datetime.now()
            )
        )
    session.commit()


def main():
    Base.metadata.create_all(session.bind)

    print("Generating employees...")
    create_employees(session, 300)

    print("Generating departments...")
    create_departments(session)

    print("Assigning employees to departments...")
    assign_employees_to_departments(session)

    print("Generating salaries...")
    create_salaries(session)


if __name__ == "__main__":
    main()