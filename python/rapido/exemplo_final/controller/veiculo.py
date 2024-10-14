from dataclasses import dataclass
from controller.pessoa import Pessoa
from controller.marca import Marca

@dataclass
class Veiculo:
    placa: str
    cor: str
    propietario: Pessoa
    marca: Marca
