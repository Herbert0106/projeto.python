# ============================================================
# AVALIAÇÃO A1 - Técnicas de Desenvolvimento de Algoritmos
# ============================================================

def verificar_etapa_escolar():
    """Estruturas Condicionais"""
    print("\n=== Verificador de Etapa Escolar ===")
    idade = int(input("Digite sua idade: "))

    if idade < 6:
        print("Você ainda não pode se matricular no Ensino Fundamental.")
    elif 6 <= idade < 15:
        print("Você pode se matricular no Ensino Fundamental.")
    elif 15 <= idade < 18:
        print("Você pode se matricular no Ensino Médio.")
    else:
        print("Você pode estudar no EJA ou cursos para adultos.")


def pares_contadores():
    """Estruturas de repetição"""
    print("\n=== PARES DE 1 A 100 (USANDO FOR) ===")
    for num in range(1, 101):
        if num % 2 == 0:
            print(num, end=" ")

    print("\n\n=== PARES DE 1 A 100 (USANDO WHILE) ===")
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1
    print("\n")


def lista_alunos():
    """Listas"""
    print("\n=== Cadastro de Alunos ===")
    alunos = []

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break

        alunos.append(nome)
        print(f"Aluno '{nome}' cadastrado!")

    print("\n=== Lista Final de Alunos ===")
    for aluno in alunos:
        print(f"- {aluno}")

    print(f"\nTotal de alunos cadastrados: {len(alunos)}")


def cadastro_notas():
    """Dicionários"""
    print("\n=== Cadastro de Notas dos Alunos ===")

    notas = {}

    while True:
        aluno = input("Nome do aluno (ou 'parar' para encerrar): ")
        if aluno.lower() == "parar":
            break

        nota = float(input(f"Digite a nota de {aluno}: "))
        notas[aluno] = nota

    print("\n=== Notas Cadastradas ===")
    for aluno, nota in notas.items():
        print(f"{aluno}: {nota}")

    if notas:
        media = sum(notas.values()) / len(notas)
        print(f"\nMédia geral da turma: {media:.2f}")
    else:
        print("Nenhuma nota cadastrada.")


# ============================================================
#                     MENU PRINCIPAL
# ============================================================

def main():
    while True:
        print("\n=====================================")
        print("      MENU - AVALIAÇÃO A1")
        print("=====================================")
        print("1 - Verificar etapa escolar (Condicionais)")
        print("2 - Mostrar pares de 1 a 100 (Repetição)")
        print("3 - Cadastro de alunos (Listas)")
        print("4 - Cadastro de notas (Dicionários)")
        print("0 - Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            verificar_etapa_escolar()
        elif opcao == "2":
            pares_contadores()
        elif opcao == "3":
            lista_alunos()
        elif opcao == "4":
            cadastro_notas()
        elif opcao == "0":
            print("Encerrando o programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

