import json
from collections import defaultdict
from typing import List
from models import Employee


def save_report_by_department_json(
    employees: List[Employee], report_result: dict[str, int], filename: str
) -> None:
    """
    Сохраняет отчет (например, payout) в JSON, сгруппировав данные по отделам.

    :param employees: Список сотрудников.
    :param report_result: Словарь с результатом отчета, ключ - email, значение - число (например, зарплата).
    :param filename: Имя файла для сохранения JSON.
    """
    dept_map = defaultdict(list)
    email_to_dept = {emp.email: emp.department for emp in employees}

    for email, value in report_result.items():
        department = email_to_dept.get(email, "Неизвестный отдел")
        dept_map[department].append({"email": email, "value": value})

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(dept_map, f, ensure_ascii=False, indent=4)


def print_report_by_department(
    employees: List[Employee],
    report_result: dict[str, int],
    value_name: str = "Значение",
) -> None:
    """
    Выводит в консоль отчет, сгруппированный по отделам.

    :param employees: Список сотрудников.
    :param report_result: Словарь с результатом отчета, ключ - email, значение - число.
    :param value_name: Название выводимого значения (например, "Зарплата", "Выплата").
    """
    dept_map = defaultdict(list)
    for emp in employees:
        dept_map[emp.department].append(emp.email)

    print(f"Отчет по значению `{value_name.lower()}` по отделам:")
    for department, emails in dept_map.items():
        print(f"\nОтдел: {department}")
        max_email_len = max(len(email) for email in emails)
        for email in emails:
            value = report_result.get(email, 0)
            print(f"  {email.ljust(max_email_len)} : {value}")
