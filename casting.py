from constant import REPLACEMENT_VALUES


def replace_values(name_field: str) -> str:
    if name_field.strip() in REPLACEMENT_VALUES:
        return name_field.strip()
    else:
        for key, aliases in REPLACEMENT_VALUES.items():
            if name_field.strip() in aliases:
                return key

    raise ValueError(f"Неизвестное поле: {name_field}")


def cast_names(headers: list[str]):
    return [replace_values(name) for name in headers]
