menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Você escolheu a opção depósito")

        valor_depositado = float(input("Quanto você deseja depositar?"))

        if valor_depositado > 0:

            saldo = saldo + valor_depositado
        else:
            print("Valor inválido, por favor repita a operação.")

        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"

    elif opcao == "s":
        print(f"Você escolheu a opção Sacar. Você possui {LIMITE_SAQUES} restantes")

        valor_saque = float(input("Quanto você deseja sacar?"))

        if LIMITE_SAQUES > 0:

            if valor_saque > saldo:
                print("Valor do saque não permitido, realizar operação novamente")
            elif valor_saque > 500:
                print("Valor do saque não permitido, realizar operação novamente")
            elif valor_saque < 0:
                print("Valor do saque não permitido, realizar operação novamente")
            else:
                saldo = saldo - valor_saque
                LIMITE_SAQUES = LIMITE_SAQUES - 1
                extrato += f"Depósito: R$ {valor_saque:.2f}\n"
        
        else:
            print("limite de saques diários já utilizado")
    
    elif opcao == "e":
        print("Você escolheu a opção extrato.")

        print(f"Você realizou as seguintes transações \n\n {extrato} \n\n e seu saldo final é {saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Selecione novamente")
    