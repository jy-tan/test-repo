from utils.format_text import format_currency, make_camelcase, count_words

def test_count_words():
    # Test counting words in a string with multiple words separated by spaces
    assert count_words("This is a test string") == 5
    
    # Test counting words in a single-word string
    assert count_words("Hello") == 1

def test_count_words_empty_string():
    # Test that an empty string returns 0 words
    assert count_words("") == 0

def test_count_words_with_leading_trailing_spaces():
    # Test string with leading spaces
    assert count_words("   hello world") == 2
    
    # Test string with trailing spaces
    assert count_words("hello world   ") == 2
    
    # Test string with both leading and trailing spaces
    assert count_words("   hello beautiful world   ") == 3

def test_count_words_multiple_spaces():
    # Test counting words in a string with multiple spaces between words
    assert count_words("This   is  a    test    string") == 5
    
    # Test with a mix of different whitespace characters
    assert count_words("Words  with\t\tmultiple \n spaces") == 4
    
    # Test with spaces at the beginning and end as well as between words
    assert count_words("   Multiple   spaces   between   words   ") == 4

def test_count_words_with_various_whitespace():
    # Test with mixed whitespace characters (spaces, tabs, newlines)
    assert count_words("word1 word2\tword3\nword4") == 4
    
    # Test with consecutive mixed whitespace characters
    assert count_words("word1  \t\n  word2") == 2
    
    # Test with mixed whitespace at beginning, middle, and end
    assert count_words("\t  word1 \n word2  \t") == 2
    
    # Test with a more complex example containing multiple types of whitespace
    text_with_mixed_whitespace = """This is a
    multi-line text with\ttabs
    and    multiple    spaces"""
    assert count_words(text_with_mixed_whitespace) == 10

def test_count_words_whitespace_only():
    # Test string with only spaces
    assert count_words("    ") == 0
    
    # Test string with mixed whitespace characters (spaces, tabs, newlines)
    assert count_words("  \t  \n  \r  ") == 0
    
    # Test string with a single whitespace character
    assert count_words(" ") == 0

