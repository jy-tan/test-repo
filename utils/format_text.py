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

def count_words(text):
    return len(text.split())

def capitalize_words(text):
    return re.sub(r'\S+', lambda m: m.group(0).capitalize(), text)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()
