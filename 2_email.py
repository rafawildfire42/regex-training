import re

email = "rafael@gmail.com".lower()

email_pattern = r"^\w+@[a-z0-9]+\.[a-z]+$"

def check_email(email: str):
    is_valid_email = re.match(email_pattern, email)
    return bool(is_valid_email)

print(check_email(email))