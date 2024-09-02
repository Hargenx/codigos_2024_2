import re

def validate_email(email: str) -> bool:
    '''Valida e-mail usando regex pattern.
    Args:
        email: O endereço de email para validação.
    Returns:
        True se o endereço de email é valido, se não for retorna False.'''
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.match(regex, email)
    return bool(match)

if __name__ == "__main__":
    email1 = "raphael.jesus@estacio.com"
    email2 = "invalid_email@example"
    email3 = "valid@email.co.uk"

    print(validate_email(email1))
    print(validate_email(email2))
    print(validate_email(email3))