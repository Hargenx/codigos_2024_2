import re

def valida_email(email: str) -> bool:
    '''Valida e-mail usando regex pattern.
    Args:
        email: O endereço de email para validação.
    Returns:
        True se o endereço de email é valido, se não for retorna False.'''
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$"
    match = re.match(regex, email)
    return bool(match)

if __name__ == "__main__":
    email_teste = ["raphael.jesus@estacio.br",
    "invalid_email@example",
    "valid@email.co.uk",
    "valido@email.com.br",
    "invalido.com.br"]

    for email in email_teste:
        print(valida_email(email))

