import re

def is_valid_email(email:str) -> bool:
    email = email.lower()
    pattern = r"^[^@]+@[^@]+\.[^@]+$"

    match = re.match(pattern, email)

    if match:
        return True
    else:
        return False

print(is_valid_email("user@example.com"))
print(is_valid_email("userexample.com"))