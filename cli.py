import argparse

from register import register_formatter


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=str,
        nargs="*",
        help="Пути к файлам для обработки"
    )
    parser.add_argument(
        "--report",
        type=str,
        default="output.txt",
        help="Введите имя файла для сохранения отчета"
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        default="payout",
        help=(f"Выберите формат отчета:\n"
              f"{register_formatter.help()}\n")
    )
    return parser
