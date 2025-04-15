from utils.format_text import format_currency, make_camelcase, count_words
import textwrap


def test_count_words():
    # Test counting words in a simple string with spaces
    assert count_words("hello world") == 2

    # Test counting words in a longer sentence
    assert count_words("this is a test sentence with seven words") == 8

    # Test counting words in a string with mixed case
    assert count_words("Hello World Test String") == 4

    # Test counting words in a string with punctuation (punctuation doesn't affect word count)
    assert count_words("Hello, world! How are you?") == 5

    # Test counting words in an empty string
    assert count_words("") == 0


def test_count_words_with_leading_trailing_spaces():
    # Test with leading spaces
    assert count_words("   hello world") == 2

    # Test with trailing spaces
    assert count_words("hello world   ") == 2

    # Test with both leading and trailing spaces
    assert count_words("   hello beautiful world   ") == 3

    # Test with excessive spaces on both ends
    assert count_words("      text with spaces      ") == 3


def test_count_words_multiple_spaces():
    # Test counting words with double spaces between words
    assert count_words("hello  world") == 2

    # Test counting words with varying numbers of spaces
    assert count_words("this   has    different     spaces") == 4

    # Test counting words with extreme spacing
    assert count_words("words          with          many          spaces") == 4

    # Test counting with a mix of single and multiple spaces
    assert count_words("one space two  spaces three   spaces") == 6

    # Test with spaces at the beginning, middle, and end
    assert count_words("  multiple  spaces  at  different  positions  ") == 5


def test_count_words_with_various_whitespace():
    # Test counting words separated by tabs
    assert count_words("hello\tworld\tpython") == 3

    # Test counting words separated by newlines
    assert count_words("hello\nworld\npython") == 3

    # Test counting words separated by carriage returns
    assert count_words("hello\rworld\rpython") == 3

    # Test counting words with mixed whitespace characters
    assert count_words("hello\tworld\npython\r testing") == 4

    # Test counting words with consecutive different whitespace characters
    assert count_words("hello\t\nworld  \r\n  python") == 3

    # Test with a complex real-world example containing various whitespace
    text_with_mixed_whitespace = textwrap.dedent(
        """This is a paragraph
    with multiple lines\tand tabs
    to test the word\rcounting functionality."""
    )
    assert count_words(text_with_mixed_whitespace) == 15
