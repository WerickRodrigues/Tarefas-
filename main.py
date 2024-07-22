tarefas = []

def adicionar_tarefas(tarefa):
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" foi adicionada.')

def listar_tarefas():
    if not tarefas:
        print('Você ainda não possui tarefas.')
    else:
        print('Tarefas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def editar_tarefas(indice, nova_tarefa):
    try:
        tarefas[indice - 1] = nova_tarefa
        print(f'Tarefa editada para "{nova_tarefa}".')
    except IndexError:
        print('Índice inválido.')

def remover_tarefa(indice):
    try:
        tarefa_removida = tarefas.pop(indice - 1)
        print(f'Tarefa "{tarefa_removida}" foi removida.')
    except IndexError:
        print('Índice inválido.')

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Editar tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input('Digite a tarefa: ')
            adicionar_tarefas(tarefa)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            listar_tarefas()
            try:
                indice = int(input('Digite o número da tarefa a ser removida: '))
                remover_tarefa(indice)
            except ValueError:
                print('Por favor, digite um número válido.')
        elif escolha == '4':
            listar_tarefas()
            try:
                indice = int(input('Digite o número da tarefa a ser editada: '))
                nova_tarefa = input('Digite a nova tarefa: ')
                editar_tarefas(indice, nova_tarefa)
            except ValueError:
                print('Por favor, digite um número válido.')
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Escolha inválida, por favor, escolha uma opção válida.')
menu()
