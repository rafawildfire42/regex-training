import re

phone_number = "(063) 99947-4437"

ddd_pattern = r"^\([0]\d{2}\)\s"
number_pattern = r"[9][8-9]\d{3}-\d{4}$"
phone_number_pattern = ddd_pattern + number_pattern

def check_phone_number(phone_number: str):
    matches_found = re.findall(phone_number_pattern, phone_number)
    is_valid_number = bool(matches_found)
    return is_valid_number

print("Número de celular:", phone_number)
print("O número é válido?", check_phone_number(phone_number))