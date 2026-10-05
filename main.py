# Aluno 1 - Cadastro e Entidades Base
# Cadastro da Empresa/Startup
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

# Aluno 2 - Matriz 2D de Estado
# Matriz 2D representando o estado dos setores de acesso
# 1 = Acesso permitido
# 0 = Acesso bloqueado
matriz_acesso = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
]


def mostrar_empresa():
    print("\n--- Dados da Empresa ---")
    print("Empresa:", empresa["nome"])
    print("Segmento:", empresa["segmento"])
    print("Produto:", empresa["produto"])


def mostrar_recursos():
    print("\n--- Recursos em Operação ---")
    for recurso in recursos:
        print("-", recurso)


def mostrar_acessos():
    print("\n--- Matriz de Controle de Acesso ---")
    for linha in matriz_acesso:
        print(linha)


# Aluno 3 - Menu Interativo com Validação

def menu():
    while True:
        print("\n===== CONTROLE DE ACESSO =====")
        print("1 - Ver dados da empresa")
        print("2 - Ver recursos em operação")
        print("3 - Ver matriz de acesso")
        print("4 - Sair")

        opcao = input("Digite uma opção: ").strip()

        if opcao == "":
            print("Erro: o campo não pode ficar vazio!")
        elif opcao == "1":
            mostrar_empresa()
        elif opcao == "2":
            mostrar_recursos()
        elif opcao == "3":
            mostrar_acessos()
        elif opcao == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida! Digite uma opção de 1 a 4.")


if __name__ == "__main__":
    menu()


