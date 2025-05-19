from utils.format_text import (
    format_currency,
    make_camelcase,
    count_words,
    capitalize_words,
    remove_extra_spaces,
    slugify,
)


def test_format_currency():
    # Test formatting an integer
    assert format_currency(1234) == "$1,234.00"

    # Test formatting a float with fewer than two decimal places
    assert format_currency(1234.5) == "$1,234.50"

    # Test formatting a float with more than two decimal places (rounding expected)
    assert format_currency(1234.567) == "$1,234.57"

    # Test formatting of a large number with commas for separation
    assert format_currency(1234567890.12) == "$1,234,567,890.12"


def test_count_words_multiple_words():
    text = "This is a sentence with multiple words"
    assert count_words(text) == 7


def test_capitalize_words_multiple_lowercase_words():
    text = "this is a test"
    assert capitalize_words(text) == "This Is A Test"


def test_remove_extra_spaces_multiple_spaces():
    text = "This   is  a    sentence  with     extra   spaces"
    assert remove_extra_spaces(text) == "This is a sentence with extra spaces"


def test_remove_extra_spaces_leading_trailing():
    text = "   This is a sentence with leading and trailing spaces   "
    assert (
        remove_extra_spaces(text)
        == "This is a sentence with leading and trailing spaces"
    )


def test_slugify_simple_string():
    assert slugify("Hello World") == "hello-world"


def test_slugify_unicode_characters():
    assert slugify("你好世界") == ""


def test_slugify_empty_string():
    assert slugify("") == ""
