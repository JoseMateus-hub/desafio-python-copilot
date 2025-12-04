# Resolvendo Códigos em Python com o GitHub Copilot / ChatGPT
# Autor: José Mateus
# Projeto da DIO - Desafio "Resolvendo códigos com Python e Copilot"


def concatenar_dados():
    print("\n🟦 Exercício 1 - Concatenando Dados")
    nome = input("Digite um nome: ")
    sobrenome = input("Digite um sobrenome: ")
    resultado = f"{nome} {sobrenome}"
    print(f"Resultado: {resultado}\n")


def repetindo_textos():
    print("\n🟧 Exercício 2 - Repetindo Textos")
    texto = input("Digite uma palavra ou frase: ")
    vezes = int(input("Quantas vezes deseja repetir? "))
    resultado = texto * vezes
    print(f"Resultado: {resultado}\n")


def operacoes_simples():
    print("\n🟨 Exercício 3 - Operações Matemáticas Simples")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    print(f"Soma: {n1 + n2}")
    print(f"Subtração: {n1 - n2}")
    print(f"Multiplicação: {n1 * n2}")
    print(f"Divisão: {n1 / n2 if n2 != 0 else 'Impossível dividir por zero'}\n")


def verificar_par_impar():
    print("\n🟩 Exercício 4 - Verificando Par ou Ímpar")
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("O número é PAR.\n")
    else:
        print("O número é ÍMPAR.\n")


def calcular_media():
    print("\n🟦 Exercício 5 - Calculando Média")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3
    print(f"A média final é: {media:.2f}\n")


def verificar_palindromo():
    print("\n🟪 Exercício 6 - Verificando Palíndromos")
    palavra = input("Digite uma palavra: ")

    if palavra == palavra[::-1]:
        print("É um palíndromo!\n")
    else:
        print("Não é um palíndromo.\n")


def menu():
    while True:
        print("\n==============================")
        print("     DESAFIO PYTHON DIO")
        print("   GitHub Copilot / ChatGPT  ")
        print("==============================")
        print("1 - Concatenando Dados")
        print("2 - Repetindo Textos")
        print("3 - Operações Simples")
        print("4 - Verificar Par/Ímpar")
        print("5 - Calculando Média")
        print("6 - Verificando Palíndromo")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            concatenar_dados()
        elif opcao == "2":
            repetindo_textos()
        elif opcao == "3":
            operacoes_simples()
        elif opcao == "4":
            verificar_par_impar()
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            verificar_palindromo()
        elif opcao == "0":
            print("\nSaindo... Até mais! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Inicializa o programa
menu()
