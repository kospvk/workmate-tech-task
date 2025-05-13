import dataclasses as dt


@dt.dataclass
class Employee:
    id: str
    email: str
    name: str
    department: str
    hours_worked: str
    hourly_rate: str


EMPLOYEE_ALIASES = {
    "rate": "hourly_rate",
    "salary": "hourly_rate",
}
