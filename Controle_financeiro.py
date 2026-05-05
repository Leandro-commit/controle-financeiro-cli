def formatar_real(valor):
    return f"{valor:.2f}".replace(".", ",")


saldo = 0
movimentacoes = []

print("PLANILHA PESSOAL DE CONTROLE FINANCEIRO.")

while True:
    print("\n1 - Adicionar entrada (ganho)")
    print("2 - Adicionar saída (gasto)")
    print("3 - Ver saldo atual")
    print("4 - Listar movimentações")
    print("5 - Sair\n")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("*Digite uma opção válida (entre 1 e 5)*")
        continue

    if opcao not in (1, 2, 3, 4, 5):
        print("*Opção inválida (escolha entre 1 e 5)*")
        continue

    # ---ENTRADA---
    elif opcao == 1:
        while True:
            try:
                entrada = float(input("Valor da entrada: R$ ").replace(",", "."))
                break
            except ValueError:
                print("Digite um valor válido!")

        descricao = input("Adicione uma descrição: ")

        movimentacao = {"tipo": "entrada", "valor": entrada, "descricao": descricao}

        movimentacoes.append(movimentacao)
        saldo += entrada

        print("Entrada adicionada!")

    # ---SAÍDA---
    elif opcao == 2:
        while True:
            try:
                saida = float(input("Valor da saída: R$ ").replace(",", "."))
                break
            except ValueError:
                print("Digite um valor válido!")

        if saida > saldo:
            print("Sua retirada é maior que o saldo atual!")
            continue

        descricao = input("Adicione uma descrição: ")

        movimentacao = {"tipo": "saida", "valor": saida, "descricao": descricao}

        movimentacoes.append(movimentacao)
        saldo -= saida

        print(f"Retirada com sucesso! Saldo atual: R$ {formatar_real(saldo)}")

    # ---SALDO---
    elif opcao == 3:
        print(f"Saldo atual: R$ {formatar_real(saldo)}")

    # ---HISTÓRICO---
    elif opcao == 4:
        if not movimentacoes:
            print("Nenhuma movimentação registrada.")
        else:
            print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---\n")
            for i, mov in enumerate(movimentacoes, start=1):
                print(
                    f"{i}. {mov['tipo'].capitalize()} - R$ {formatar_real(mov['valor'])} - {mov['descricao']}"
                )

    # ---SAIR---
    elif opcao == 5:
        print("Encerrando o sistema...")
        break
