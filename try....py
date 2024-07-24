print("Augusto,M & Vallez,S.A.")

print("\n")

lista_funcionarios = [

]

id_global = 1234567

print("\n")

def cadastrar_funcionario(): # Define the function before it is called

   colaborador = {}
   colaborador['id'] = id_global # Use the global id
   colaborador['nome'] = input("Digite o nome do funcionário: ")
   colaborador['setor'] = input("Digite o setor do funcionário: ")
   colaborador['salario'] = float(input("Digite o salário do funcionário: "))

   lista_funcionarios.append(colaborador.copy()) # Use the correct variable name
   print("Funcionário cadastrado com sucesso!")

   print("\n")

def consultar_funcionarios():
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

def remover_funcionario():
 
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        for i, funcionario in enumerate(lista_funcionarios):
            if funcionario['id'] == id_remover:
                del lista_funcionarios[i]
                print("Funcionário removido com sucesso!")
                return # Exit the function after removing

        print("Id inválido.")

while True:
    opcao = input("""
    Menu Principal:
    1. Cadastrar Funcionário
    2. Consultar Funcionário(s)
    3. Remover Funcionário
    4. Sair
    Digite o número da opção desejada:""")

    if opcao == '1':
        id_global += 1
        cadastrar_funcionario()
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        print("Encerrando o programa...")
        break # Exit the main loop
    else:
        print("Opção inválida.")
