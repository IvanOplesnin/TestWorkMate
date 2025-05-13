import pytest
from register import RegisterFormatter, register_formatter
from employee import Employee


def test_help_initial_empty():
    reg = RegisterFormatter()
    assert reg.help() == ""


def test_add_func_and_get_formatter_returns_function():
    reg = RegisterFormatter()

    @reg.add_func('test')
    def formatter_a(employees: list[Employee]) -> str:
        return 'A'

    assert reg.FORMATTERS['test'] is formatter_a
    assert reg.get_formatter('test') is formatter_a


def test_get_formatter_invalid_name_raises():
    reg = RegisterFormatter()
    with pytest.raises(ValueError) as exc:
        reg.get_formatter('no_such')
    assert 'Неизвестный форматтер: no_such' in str(exc.value)


def test_help_shows_last_registered_doc():
    reg = RegisterFormatter()

    @reg.add_func('first')
    def fmt1(employees: list[Employee]) -> str:
        """First doc"""
        return '1'

    @reg.add_func('second')
    def fmt2(employees: list[Employee]) -> str:
        """Second doc"""
        return '2'

    result = reg.help()
    assert result.strip() == 'first: First doc\nsecond: Second doc'


def test_register_multiple_and_get_all():
    reg = RegisterFormatter()

    @reg.add_func('f1')
    def f1(emp_list: list[Employee]) -> str:
        """Doc1"""
        return 'f1'

    @reg.add_func('f2')
    def f2(emp_list: list[Employee]) -> str:
        """Doc2"""
        return 'f2'

    assert 'f1' in reg.FORMATTERS and 'f2' in reg.FORMATTERS
    assert reg.get_formatter('f1') is f1
    assert reg.get_formatter('f2') is f2
