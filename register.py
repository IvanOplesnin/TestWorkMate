from typing import Callable

from employee import Employee


class RegisterFormatter:
    def __init__(self):
        self.FORMATTERS = {}

    def help(self) -> str:
        help_msg = ""
        for name, func in self.FORMATTERS.items():
            help_msg = f"{name}: {func.__doc__.strip()}\n\n"

        return help_msg

    def add_func(self, name):
        def wrapper(func):
            self.FORMATTERS[name] = func
            return func

        return wrapper

    def get_formatter(self, formatter_name: str) -> Callable[[list[Employee]], str] | None:
        func = self.FORMATTERS.get(formatter_name, None)
        if func is None:
            raise ValueError(f"Неизвестный форматтер: {formatter_name}")
        else:
            return func


register_formatter = RegisterFormatter()