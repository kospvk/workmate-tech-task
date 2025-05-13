from src.csv_parser import parse_csv_file


def test_parse_csv_file():
    filename = "tests/test_employees.csv"
    employees = list(parse_csv_file(filename))
    assert len(employees) > 0
    assert isinstance(employees[0], dict)
    assert employees[0]["id"] == "1"
