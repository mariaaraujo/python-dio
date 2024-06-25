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
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: ").replace(",", "."))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: ").replace(",", "."))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Saldo insuficiente!").replace(",", ".")
        elif limite_excedido:
            print("Limite de saques excedido!")
        elif saque_excedido:
            print("Você já atingiu o limite de saques!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "e":
        print("\n ============= Extrato ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida!")
