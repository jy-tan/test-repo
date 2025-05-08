import re
import inflect

p = inflect.engine()

def make_camelcase(text):
    words = text.lower().split()
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def format_currency(number):
    return f"${number:,.2f}"

def format_percentage(number):
    return f"{number:.2f}%"

def format_date(date):
    return date.strftime("%Y-%m-%d")

def format_time(time):
    return time.strftime("%H:%M:%S")

def conditional_plural(word, count, include_count=True):
    """
    Returns the singular or plural form of a word based on the count.
    Optionally includes the count in the output string. Handles basic type checking.
    """
    if not isinstance(count, (int, float)):
        raise TypeError("Count must be a number.")
    if not isinstance(word, str):
        raise TypeError("Word must be a string.")

    plural_form = p.plural(word, count)

    if include_count:
        # Format the count nicely (e.g., remove .0 for whole numbers)
        formatted_count = int(count) if count == int(count) else count
        return f"{formatted_count} {plural_form}"
    else:
        return plural_form
