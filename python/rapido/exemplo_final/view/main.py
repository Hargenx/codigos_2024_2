from datetime import date
from controller.pessoa import Pessoa
from controller.marca import Marca
from controller.veiculo import Veiculo

# Criando uma instância de Pessoa
pessoa1 = Pessoa(
    cpf=12345678900, nome="Raphael", nascimento=date(1984, 7, 26), oculos=True
)

# Criando uma instância de Marca
marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

# Criando uma instância de Veiculo
veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, marca=marca1)

print("Informações do Pessoa:")
print(f"CPF: {pessoa1.cpf}")
print(f"Nome: {pessoa1.nome}")
print(f"Nascimento: {pessoa1.nascimento}")
print(f"Usa óculos: {pessoa1.oculos}")

print("\nInformações da Marca:")
print(f"ID: {marca1.id}")
print(f"Nome: {marca1.nome}")
print(f"Sigla: {marca1.sigla}")

print("\nInformações do Veículo:")
print(f"\tPlaca: {veiculo1.placa}")
print(f"\tCor: {veiculo1.cor}")
print("Proprietário:")
print(f"\tCPF: {veiculo1.proprietario.cpf}")
print(f"\tNome: {veiculo1.proprietario.nome}")
print("Marca:")
print(f"\tID: {veiculo1.marca.id}")
print(f"\tNome: {veiculo1.marca.nome}")
print(f"\tSigla: {veiculo1.marca.sigla}")
