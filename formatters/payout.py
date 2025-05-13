from employee import Employee
from register import register_formatter


@register_formatter.add_func("payout")
def payout(employees: list[Employee]) -> str:
    """
    Вывод данных по выплате сотрудников.
    """

    name_width = max(len(e.name) for e in employees)

    header = (
        f"{'':14} "
        f"{'name':{name_width}} "
        f"{'hours':<8} "
        f"{'rate':<6} "
        f"{'payout':<10}\n"
    )

    sorted_emps = sorted(employees, key=lambda e: (e.department, e.rate))

    output = header
    current_dept = None
    dept_hours = 0
    dept_payout = 0

    for emp in sorted_emps:
        if emp.department != current_dept:
            if current_dept is not None:
                output += (
                    f"{'':14} "
                    f"{'':{name_width}} "
                    f"{dept_hours:<8} "
                    f"{'':<6} "
                    f"${dept_payout:<9}\n"
                )
                dept_hours = dept_payout = 0

            current_dept = emp.department
            output += f"{emp.department}\n"

        payout = emp.payout
        dept_hours += emp.hours_worked
        dept_payout += payout

        output += (
            f"{'-' * 14} "
            f"{emp.name:{name_width}} "
            f"{emp.hours_worked:<8} "
            f"{emp.rate:<6} "
            f"${payout:<9}\n"
        )

    output += (
        f"{'':14} "
        f"{'':{name_width}} "
        f"{dept_hours:<8} "
        f"{'':<6} "
        f"${dept_payout:<9}\n"
    )

    return output


