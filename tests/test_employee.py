import pytest
from employee import Employee


def test_employee_init_valid():
    e = Employee(
        id="32",
        name="Ivan",
        email="ivan@gmail.com",
        department="Sales",
        hours_worked="200",
        rate="200"
    )
    assert isinstance(e.id, int)
    assert e.id == 32
    assert e.name == "Ivan"
    assert e.email == "ivan@gmail.com"
    assert e.department == "Sales"
    assert isinstance(e.hours_worked, int)
    assert e.hours_worked == 200
    assert isinstance(e.rate, int)
    assert e.rate == 200


def test_employee_payout():
    e = Employee(
        id="32",
        name="Ivan",
        email="ivan@gmail.com",
        department="Sales",
        hours_worked="200",
        rate="200"
    )
    e2 = Employee(
        id="1",
        name="Polina",
        email="polina@gmail.com",
        department="HR",
        hours_worked="40",
        rate="5"
    )
    assert e.payout == 40000
    assert e2.payout == 200


@pytest.mark.parametrize(
    "field, value", [
        ('id', 'abc'),
        ('hours_worked', 'notanumber'),
        ('rate', '3.14'),
    ]
)
def test_employee_init_invalid_numeric(field, value):
    kwargs = {
        'id': '1',
        'name': 'Test',
        'email': 'test@example.com',
        'department': 'HR',
        'hours_worked': '8',
        'rate': '20'
    }
    kwargs[field] = value
    with pytest.raises(ValueError):
        Employee(**kwargs)
