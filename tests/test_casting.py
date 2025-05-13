import pytest
from constant import REPLACEMENT_VALUES
from casting import replace_values, cast_names


def test_replace_canonical():
    for key in REPLACEMENT_VALUES:
        assert replace_values(key) == key
        assert replace_values(f"  {key}   ") == key


@pytest.mark.parametrize(
    "input, output", [
        (alias, key) for key, aliases in REPLACEMENT_VALUES.items()
        for alias in aliases
    ]
)
def test_replace_alternative(input, output):
    assert replace_values(input) == output
    assert replace_values(f"  {input}   ") == output


def test_replace_values_unknown_field():
    with pytest.raises(ValueError) as exc:
        replace_values('unknown_field')
    assert 'Неизвестное поле' in str(exc.value)
    assert 'unknown_field' in str(exc.value)


@pytest.mark.parametrize(
    "headers, expected", [
        (
                ['id', ' hourly_rate', 'name ', ' salary ', 'department'],
                ['id', 'rate', 'name', 'rate', 'department']
        ),
        (
                ["  id   ", "name ", "   salary   ", "rate   ", "   hourly_rate "],
                ['id', 'name', 'rate', 'rate', 'rate']
        )
    ]
)
def test_cast_names_success(headers, expected):
    assert cast_names(headers) == expected


def test_cast_names_with_unknown():
    with pytest.raises(ValueError):
        cast_names(['id', 'unknown_column', 'name'])
