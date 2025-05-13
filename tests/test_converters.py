from src.converters import dict_to_dataclass
from src.models import Employee


def test_dict_to_dataclass():
    data = {
        "email": "mia@example.com",
        "name": "Mia Young",
        "department": "Sales",
        "hours_worked": "160",
        "hourly_rate": "37",
        "id": "203",
    }
    assert isinstance(dict_to_dataclass(data, Employee), Employee)
