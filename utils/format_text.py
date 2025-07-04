import re

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

def count_words(text, sep=" "):
    return len(text.split(sep))

def capitalize_words(text):
    return re.sub(r'\S+', lambda m: m.group(0).capitalize(), text)

def make_snake_case(text):
    return re.sub(r'\s+', '_', text).lower()

def make_kebab_case(text):
    return re.sub(r'\s+', '-', text).lower()
