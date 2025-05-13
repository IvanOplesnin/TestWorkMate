import pytest
from employee import Employee
from csv_reader import (
    create_employee,
    process_first_line,
    add_employee_to_list_from_file,
    processing_files
)

HEADER = "id,email,name,department,hours_worked,hourly_rate"
LINE = "1,alice@example.com,Alice Johnson,Marketing,160,50"
LINE_2 = "2,bob@example.com,Bob Smith,Design,150,40"

HEADER_2 = "department,id,email,name,hours_worked,rate"
LINE_3 = "HR,101,grace@example.com,Grace Lee,160,45"


@pytest.mark.parametrize(
    "header,expected", [
        (HEADER,
         ["id", "email", "name", "department", "hours_worked", "rate"]),
        (HEADER_2,
         ["department", "id", "email", "name", "hours_worked", "rate"])
    ]
)
def test_process_first_line(header, expected):
    assert process_first_line(header) == expected


def test_create_employee_correct_fields():
    names = ["id", "email", "name", "department", "hours_worked", "rate"]
    e = create_employee(LINE, names)
    assert isinstance(e, Employee)
    assert e.id == 1
    assert e.email == "alice@example.com"
    assert e.name == "Alice Johnson"
    assert e.department == "Marketing"
    assert e.hours_worked == 160
    assert e.rate == 50


def test_add_employee_to_list_from_file(tmpdir):
    file = tmpdir.join("test.csv")
    content = f"{HEADER}\n{LINE}\n{LINE_2}"
    file.write(content)

    emps = []
    add_employee_to_list_from_file(emps, file)
    assert len(emps) == 2
    emp = emps[0]
    assert isinstance(emp, Employee)
    assert emp.name == 'Alice Johnson'
    assert emp.rate == 50


def test_processing_files_writes_and_returns(tmpdir):
    f1 = tmpdir.join("test.csv")
    f2 = tmpdir.join("test_2.csv")
    f1.write_text(HEADER + '\n' + LINE + '\n' + LINE_2 + '\n', encoding='utf-8')

    f2.write_text(HEADER_2 + '\n' + LINE_3 + '\n', encoding='utf-8')

    # Создаем небольшую функцию-форматтер, который просто возвращает число сотрудников
    def dummy_formatter(employees: list[Employee]) -> str:
        return f"COUNT={len(employees)}"

    report = tmpdir.join("report.txt")
    out_str = processing_files(
        filename=[str(f1), str(f2)],
        report=str(report),
        format_function=dummy_formatter,
    )

    assert out_str == "COUNT=3"
    assert report.read_text(encoding='utf-8') == "COUNT=3"
