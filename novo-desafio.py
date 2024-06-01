import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        extrato += f"Depósito: R$ {valor:.2f}\n"
        saldo += valor
    else :
        print("Operação falhou! O valor informado é inválido.\n")   

    return saldo, extrato     

def sacar(*, saldo, valor, extrato, limite, limite_saques):
    
    if limite_saques > 0:  
        if valor <= limite:
            if valor <= saldo:
                extrato += f"Saque R$ {valor:.2f}\n"
                saldo -= valor
                limite_saques -= 1
            else:
                print("Operação falhou! Você não tem saldo suficiente.")
        else:
            print("Operação falhou! O valor do saque excede o limite.")            
    else:
        print("Operação falhou! Número máximo de saques excedidos.") 

    return saldo, extrato    

def mostrar_extrato(saldo, extrato):
 
    if extrato != "":
        string_extrato = " EXTRATO "
        print(string_extrato.center(42,"="))
        print(f"{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 42)
    else:
        print("Não foram realizadas movimentações.")    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario is None:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

        print("=== Usuário criado com sucesso! ===")

    else:
        print("=== Já existe usuário com este CPF! ===")
        return


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is not None:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n=== Usuário não encontrado, fluxo de criação de conta encerrado! ===")

def main():
        LIMITE_SAQUES = 3
        AGENCIA = "0001"

        saldo = 0
        limite = 500
        extrato = ""
        usuarios = []
        contas = []

        while True:
            opcao = menu()

            if opcao == "d":
                print("Depósito")
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                print("Saque")
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    limite_saques = LIMITE_SAQUES,
                )

            elif opcao == "e":
                mostrar_extrato(saldo, extrato=extrato)

            elif opcao == "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)    

            elif opcao == "nu":
                criar_usuario(usuarios)

            elif opcao == "lc":
                listar_contas(contas)            

            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")     


main()                     