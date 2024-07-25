print("\n")
print("Augusto,M & Vallez,S.A.")
"\n"
# Lista para armazenar os dados dos funcionários
lista_funcionarios = [

]

id_global = 1234567 # Variável global para rastrear os IDs dos funcionários

print("\n")

def cadastrar_funcionario(): # Função para cadastrar um novo funcionário

     global id_global
     colaborador = {}
     colaborador['id'] = id_global 
     print("---------- MENU CADASTRAR FUNCIONÁRIO ------------------")
     print(f"Id do Funcionário: {id_global}")
     colaborador['nome'] = input("Por favor entre com o nome do Funcionário: ")
     colaborador['setor'] = input("Por favor entre com o setor do Funcionário: ")
     colaborador['salario'] = float(input("Por favor entre com o salário do Funcionário: "))


     lista_funcionarios.append(colaborador.copy()) # Adiciona uma cópia dos dados do funcionário à lista
     print("Funcionário cadastrado com sucesso!")

     print("\n")

def consultar_funcionarios(): # Função para consultar e exibir informações dos funcionários
    while True:
        opcao = input("""
        Escolha uma opção de consulta:
        1. Consultar Todos
        2. Consultar por Id
        3. Consultar por Setor
        4. Retornar ao menu
        Digite o número da opção desejada:""")

        if opcao == '1':
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif opcao == '2':
            id_consulta = int(input("Digite o ID do funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print(funcionario)
                    break # Exit the loop after finding the employee
            else: # This else is associated with the for loop
                print("Funcionário não encontrado.")
        elif opcao == '3':
            setor_consulta = input("Digite o setor: ")
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_consulta:
                    print(funcionario)
        elif opcao == '4':
            print("Retornando ao menu...")
            break # Exit the while loop when returning to menu
        else:
            print("Opção inválida.")

def remover_funcionario():  # Função para remover um funcionário com base no ID
 
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        for i, funcionario in enumerate(lista_funcionarios):
            if funcionario['id'] == id_remover:
                del lista_funcionarios[i]
                print("Funcionário removido com sucesso!")
                return 

        print("Id inválido.")

while True:
    opcao = input("""
    ----------------------------------
    ----------Menu Principal----------
    1. Cadastrar Funcionário:
    2. Consultar Funcionário(s):
    3. Remover Funcionário:
    4. Sair:
    >>""")

    if opcao == '1':
        id_global += 1
        cadastrar_funcionario()
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        print("Encerrando o programa...")
        break 
    else:
        print("Opção inválida.")