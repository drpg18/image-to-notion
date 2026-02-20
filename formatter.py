from detector import detect_tables

def format_notes(text):
    return text.upper()

def format_table(image):
    tables = detect_tables(image)
    return tables
