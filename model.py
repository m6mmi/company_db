import enum
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Enum,
    String,
    Float,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Gender(enum.Enum):
    M = 'MALE'
    F = 'FEMALE'


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    birth_date = Column(DateTime, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum(Gender))
    hire_date = Column(DateTime, nullable=False)

    salaries = relationship("Salary", back_populates="employee")
    departments = relationship(
        "Department",
        secondary="departments_employees",
        back_populates="employees"
    )

    def __repr__(self):
        return f"Employee({self.id}, {self.first_name}, {self.last_name})"


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )
    employee = relationship("Employee", back_populates="salaries")

    def __repr__(self):
        return f"Salary({self.id}, {self.amount}, {self.date})"


class Department(Base):
    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(String(50))

    employees = relationship(
        "Employee",
        secondary="departments_employees",
        back_populates="departments"
    )

    def __repr__(self):
        return f"Department({self.id}, {self.name})"


department_employee = Table(
    "departments_employees",
    Base.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    ),
    Column(
        "department_id",
        Integer,
        ForeignKey("departments.id")
    ),
    Column(
        "employee_id",
        Integer,
        ForeignKey("employees.id")
    ),
    Column(
        "date",
        DateTime,
        nullable=False,
        default=datetime.now()
    )
)
