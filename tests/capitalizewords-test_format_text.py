from utils.format_text import capitalize_words

def test_capitalize_words():
    # Test capitalizing multiple words separated by spaces
    assert capitalize_words("hello world python test") == "Hello World Python Test"
    
    # The test above verifies our specific test scenario:
    # `capitalize_words` should capitalize the first letter of each word for a string with multiple words separated by spaces.
    
    # Note: Additional test scenarios will be added to this function in the future, including:
    # - Single word capitalization
    # - Handling leading/trailing spaces
    # - Handling multiple spaces between words
    # - Empty string handling
    # - Handling various whitespace characters
    # - Handling words with internal capitalization
    # - Handling non-ASCII characters

def test_capitalize_words_single_word():
    # Test capitalizing a single word
    assert capitalize_words("hello") == "Hello"
    
    # Test capitalizing a single word that's already capitalized
    assert capitalize_words("Hello") == "Hello"
    
    # Test capitalizing a single word with mixed case
    assert capitalize_words("hElLo") == "Hello"
    
    # The test above verifies our specific test scenario:
    # `capitalize_words` should capitalize the first letter of a single word for a string with one word.

def test_capitalize_words_with_leading_trailing_spaces():
    # Test capitalizing words in a string with leading and trailing spaces
    assert capitalize_words("  hello world  ") == "Hello World"
    
    # Test with multiple leading and trailing spaces
    assert capitalize_words("     python is awesome     ") == "Python Is Awesome"
    
    # Test with mixed leading and trailing spaces
    assert capitalize_words("  test   ") == "Test"

def test_capitalize_words_multiple_spaces():
    # Test capitalizing words with multiple spaces between them
    input_text = "hello    world   python     test"
    expected_output = "Hello World Python Test"
    assert capitalize_words(input_text) == expected_output
    
    # Test with a mix of single and multiple spaces
    input_text = "this  is a   test  with mixed   spacing"
    expected_output = "This Is A Test With Mixed Spacing"
    assert capitalize_words(input_text) == expected_output

def test_capitalize_words_empty_string():
    # Test that an empty string input returns an empty string
    assert capitalize_words("") == ""
    
    # This test verifies our specific test scenario:
    # `capitalize_words` should return an empty string for an empty input string.

def test_capitalize_words_with_whitespace():
    # Test with tabs between words
    assert capitalize_words("hello\tworld\tpython") == "Hello World Python"
    
    # Test with newlines between words
    assert capitalize_words("hello\nworld\npython") == "Hello World Python"
    
    # Test with a mix of spaces, tabs, and newlines
    assert capitalize_words("hello world\tpython\ntest") == "Hello World Python Test"
    
    # Test with consecutive different whitespace characters
    assert capitalize_words("hello\t\nworld  python") == "Hello World Python"

def test_capitalize_words_with_internal_capitalization():
    # Test with acronyms
    assert capitalize_words("nasa USA") == "Nasa Usa"
    
    # Test with proper nouns having specific capitalization
    assert capitalize_words("iPhone macBook") == "Iphone Macbook"
    
    # Test with a mix of regular words and words with internal capitalization
    mixed_text = "the NASA launched a new iPhone app for MacBook users"
    expected = "The Nasa Launched A New Iphone App For Macbook Users"
    assert capitalize_words(mixed_text) == expected
    
    # Test with words that should maintain internal capitalization but won't
    tech_brands = "iOS Android MacOS tvOS watchOS"
    expected_result = "Ios Android Macos Tvos Watchos"
    assert capitalize_words(tech_brands) == expected_result

def test_capitalize_words_with_non_ascii():
    # Test with accented Latin characters
    assert capitalize_words("café résumé naïve") == "Café Résumé Naïve"
    
    # Test with non-Latin script (Cyrillic and Greek)
    assert capitalize_words("привет κόσμος") == "Привет Κόσμος"
    
    # Test with mixed ASCII and non-ASCII characters
    assert capitalize_words("hello café world κόσμος") == "Hello Café World Κόσμος"
    
    # Test with lowercase and uppercase non-ASCII characters
    assert capitalize_words("ESPAÑA méxico ÖSTERREICH") == "España México Österreich"
    
    # Test with special case: German ß (which capitalizes to SS in some contexts)
    # Note: In Python 3, str.capitalize() keeps 'ß' as is, not converting to 'SS'
    assert capitalize_words("straße berlin") == "Straße Berlin"
