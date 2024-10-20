from dataclasses import dataclass


@dataclass
class Veiculo:
    placa: str
    cor: str
    cpf_proprietario: int
    id_marca: int
