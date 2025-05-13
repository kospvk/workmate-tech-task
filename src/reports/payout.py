from collections.abc import Iterable

from models import Employee
from reports.base import Report


class PayoutReport(Report):
    """
    Отчет по выплатам сотрудникам.

    Генерирует словарь с расчетом зарплат для каждого сотрудника,
    где ключ - email сотрудника, значение - сумма выплаты.
    """

    def generate(self, employees: Iterable[Employee]) -> dict[str, int]:
        payout = {}

        for employee in employees:
            payout[employee.email] = int(employee.hours_worked) * int(
                employee.hourly_rate
            )

        return payout
