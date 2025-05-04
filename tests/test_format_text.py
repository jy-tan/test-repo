from utils.format_text import format_currency, make_camelcase

def test_format_currency():
    # Test formatting an integer
    assert format_currency(1234) == "$1,234.00"

    # Test formatting a float with fewer than two decimal places
    assert format_currency(1234.5) == "$1,234.50"

    # Test formatting a float with more than two decimal places (rounding expected)
    assert format_currency(1234.567) == "$1,234.57"

    # Test handling of negative numbers
    assert format_currency(-1234.56) == "-$1,234.56"

    # Test formatting of a large number with commas for separation
    assert format_currency(1234567890.12) == "$1,234,567,890.12"
