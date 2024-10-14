from dataclasses import dataclass
from datetime import date

@dataclass
class Pessoa:
    cpf: int
    nome: str
    nascimento: date
    oculos: bool
