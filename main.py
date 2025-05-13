import argparse
from typing import Iterator

from converters import dict_to_dataclass
from csv_parser import parse_csv_file
from models import Employee, EMPLOYEE_ALIASES
from reports.payout import PayoutReport
from output import print_report_by_department, save_report_by_department_json

REPORTS = {
    "payout": PayoutReport(),
}


def parse_files(filenames: list[str]) -> Iterator[Employee]:
    for filename in filenames:
        for row_dict in parse_csv_file(filename):
            yield dict_to_dataclass(row_dict, Employee, EMPLOYEE_ALIASES)


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчетов по сотрудникам")
    parser.add_argument("files", nargs="+", help="CSV файлы с данными сотрудников")
    parser.add_argument(
        "-r", "--report", required=True, choices=REPORTS.keys(), help="Тип отчета"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="Имя файла для сохранения отчета в формате JSON",
    )
    args = parser.parse_args()

    report = REPORTS.get(args.report)
    if report is None:
        print("Такой вид отчета не реализован")
        return

    employees = list(parse_files(args.files))
    result = report.generate(employees)

    print_report_by_department(employees, result, "Зарплата")

    if args.output_file is not None:
        save_report_by_department_json(employees, result, args.output_file)
        print(f"\nОтчет сохранён в файл {args.output_file}")


if __name__ == "__main__":
    main()
