import asyncio

async def tarefa(numero: int) -> None:
    '''
    Função assíncrona para executar uma tarefa

    Args:
        numero (int): Numero da tarefa

    Returns:
        None

    '''
    print(f"Inicio da tarefa {numero}")
    await asyncio.sleep(1)
    print(f"Fim da tarefa {numero}")

async def main() -> None:
    '''
    Função principal para executar as tarefas

    Args:    
        None

    Returns:
        None

    '''
    await asyncio.gather(tarefa(1), tarefa(2), tarefa(3))

if __name__ == "__main__":
    asyncio.run(main())
