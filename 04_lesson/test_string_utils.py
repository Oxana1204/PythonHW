import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    Skypro", "Skypro"),
    ("  Hello world", "Hello world"),
    ("    Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("Test   ", "Test   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("SkyPro", "r", True),
    ("Hello", "H", True),
    ("Python", "t", True),
])
def test_contains_positive(input_str, simbol_str, expected):
    assert string_utils.contains(input_str, simbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("123", "1", True),
    ("", "", True),
    ("Test", "o", False),
])
def test_contains_negative(input_str, simbol_str, expected):
    assert string_utils.contains(input_str, simbol_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol_str, expected", [
    ("SkyPro", "Pro", "Sky"),
    ("Hello", "o", "Hell"),
    ])
def test_delete_symbol_positive(input_str, simbol_str, expected):
    assert string_utils.delete_symbol(input_str, simbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol_str, expected_exception", [
    ("123", None, TypeError),
    (123, "a", AttributeError),
    ])
def test_delete_symbol_negative(input_str, simbol_str, expected_exception):
    with pytest.raises(expected_exception):
        string_utils.delete_symbol(input_str, simbol_str)
