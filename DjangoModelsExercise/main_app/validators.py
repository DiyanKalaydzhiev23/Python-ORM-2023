def validate_age(value):
    if value > 120:
        raise ValueError("Age must be between 0 and 120")