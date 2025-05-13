import pytest

from models import Employee


@pytest.fixture
def employees():
    return [
        Employee(
            id=1,
            email="alice@example.com",
            name="Alice",
            department="HR",
            hours_worked=160,
            hourly_rate=50,
        ),
        Employee(
            id=2,
            email="bob@example.com",
            name="Bob",
            department="IT",
            hours_worked=150,
            hourly_rate=60,
        ),
        Employee(
            id=3,
            email="carol@example.com",
            name="Carol",
            department="HR",
            hours_worked=170,
            hourly_rate=55,
        ),
    ]


@pytest.fixture
def payout():
    return {
        "alice@example.com": 160 * 50,
        "bob@example.com": 150 * 60,
        "carol@example.com": 170 * 55,
    }
