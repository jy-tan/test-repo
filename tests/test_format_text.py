import pytest
from utils.format_text import make_camelcase, remove_special_characters, format_currency

def test_make_camelcase_with_leading_and_trailing_spaces():
    input_text = ' hello world '
    expected_output = 'helloWorld'
    result = make_camelcase(input_text)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"

def test_remove_special_characters():
    input_text = 'Hello, World!123'
    expected_output = 'Hello World123'
    result = remove_special_characters(input_text)
    assert result == expected_output, f"Expected '{expected_output}' but got '{result}'"

def test_format_currency():
    # Test that format_currency correctly formats a number
    result = format_currency(1234.56)
    assert result == '$1,234.56', f"Expected '$1,234.56' but got {result}"

def test_make_camelcase_with_empty_string():
    input_text = ""
    
    with pytest.raises(IndexError, match="list index out of range"):
        make_camelcase(input_text)

def test_remove_special_characters_with_accented_characters():
    input_text = 'Café Musée'
    expected_output = 'Caf Mus'
    result = remove_special_characters(input_text)
    assert result == expected_output, f"Expected '{expected_output}' but got '{result}'"

def test_format_currency_negative():
    # Test that format_currency correctly formats a negative number
    result = format_currency(-123.45)
    assert result == '$-123.45', f"Expected '$-123.45' but got {result}"

def test_format_currency_rounding():
    # Test that format_currency adheres to expected rounding behavior with half-cent values
    result = format_currency(1.135)
    assert result == '$1.14', f"Expected '$1.14' but got {result}"
