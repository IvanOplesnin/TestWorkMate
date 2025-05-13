from typing import Callable

from casting import cast_names
from employee import Employee


def create_employee(line: str, names_list: list[str]) -> Employee:
    dict_employee = {
        names_list[position]: value.strip() for position, value in enumerate(line.split(','))
    }
    return Employee(**dict_employee)


def process_first_line(first_line: str) -> list[str]:
    return cast_names(first_line.split(','))


def add_employee_to_list_from_file(list_employee: list[Employee], filename: str) -> None:
    with open(filename, 'r') as f:
        names_list = process_first_line(f.readline())
        for line in f.readlines():
            list_employee.append(create_employee(line, names_list))


def processing_files(
        filename: list[str],
        report: str,
        format_function: Callable[[list[Employee]], str]
) -> str:
    list_employee: list[Employee] = []

    for file in filename:
        add_employee_to_list_from_file(list_employee, file)

    output = format_function(list_employee)
    with open(report, 'w') as f:
        f.write(output)

    return output
