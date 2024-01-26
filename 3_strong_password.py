import re

weak_password = [
    "senha123",
    "abcde",
    "123456",
    "qwerty",
    "iloveyou",
    "aA1!"
]

strong_password = [
    "aA1!aA1!",
    "P@ssw0rd!",
    "S3gur@Senha",
    "C0digoF0rte!",
    "#S3nhaC0mpl3xa!",
    "R0ck3tSc13nc3!"
]

password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$"


def check_password(password: str):
    pattern_check = re.match(password_pattern, password)
    is_valid_password = bool(pattern_check)
    return is_valid_password


all_passwords = weak_password + strong_password

for password in all_passwords:
    password_status = "Forte" if check_password(password) else "Fraca"
    text = f"Senha: {password} - Status: {password_status}"
    print(text)
