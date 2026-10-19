empresa = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "produto": "Firewall IA",
}

recursos = [
    "Servidor",
    "Banco de Dados",
    "Firewall",
    "Sistema de Controle de Acesso",
]

matriz_acesso = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
]


def mostrar_empresa():
    print("\n--- Dados da Empresa ---")
    print(f"Empresa: {empresa['nome']}")
    print(f"Segmento: {empresa['segmento']}")
    print(f"Produto: {empresa['produto']}")


def mostrar_recursos():
    print("\n--- Recursos em Operação ---")
    for recurso in recursos:
        print(f"- {recurso}")


def mostrar_acessos():
    print("\n--- Matriz de Controle de Acesso ---")
    print("1 = Acesso permitido")
    print("0 = Acesso bloqueado")
    for linha in matriz_acesso:
        print(linha)


def mostrar_custos():
    try:
        with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
            cabecalho = arquivo.readline()
            custo_1 = arquivo.readline()
            custo_2 = arquivo.readline()
            custo_3 = arquivo.readline()
            custo_4 = arquivo.readline()

        linhas = [cabecalho, custo_1, custo_2, custo_3, custo_4]
        if any(not linha.strip() for linha in linhas):
            raise ValueError("O arquivo deve conter um cabeçalho e quatro custos.")

        custos = []
        for linha in linhas[1:]:
            recurso, valor = linha.strip().split(",", maxsplit=1)
            custos.append((recurso.strip(), float(valor.strip())))
    except (OSError, ValueError) as erro:
        print(f"Erro ao ler os custos de infraestrutura: {erro}")
        return None

    print("\n--- Cabeçalho e quatro primeiros custos ---")
    for linha in linhas:
        print(linha, end="")
    return custos


def mostrar_painel(custos):
    print("\n===== PAINEL CONSOLIDADO =====")
    mostrar_empresa()
    mostrar_acessos()

    print("\n--- Custos de Infraestrutura em Nuvem ---")
    for recurso, custo in custos:
        print(f"{recurso}: R$ {custo:.2f}")

    total = sum(custo for _, custo in custos)
    print(f"Custo total: R$ {total:.2f}")


def menu(custos=None):
    while True:
        print("\n===== CONTROLE DE ACESSO =====")
        print("1 - Ver dados da empresa")
        print("2 - Ver recursos em operação")
        print("3 - Ver matriz de acesso")
        print("4 - Ver painel consolidado")
        print("5 - Sair")

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            mostrar_empresa()
        elif opcao == "2":
            mostrar_recursos()
        elif opcao == "3":
            mostrar_acessos()
        elif opcao == "4":
            if custos is None:
                print("Painel indisponível: não foi possível carregar os custos.")
            else:
                mostrar_painel(custos)
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida! Digite uma opção de 1 a 5.")


if __name__ == "__main__":
    custos = mostrar_custos()
    menu(custos)