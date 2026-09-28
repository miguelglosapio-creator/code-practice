def menu():
    print("\n=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def calcular(operacao, numero1, numero2):
    if operacao == "1":
        return numero1 + numero2
    if operacao == "2":
        return numero1 - numero2
    if operacao == "3":
        return numero1 * numero2
    if operacao == "4":
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return numero1 / numero2
    raise ValueError("Operação inválida.")


def main():
    while True:
        menu()
        operacao = input("Escolha uma operação: ").strip()

        if operacao == "0":
            print("Programa encerrado.")
            break

        if operacao not in {"1", "2", "3", "4"}:
            print("Opção inválida. Tente novamente.")
            continue

        numero1 = ler_numero("Digite o primeiro número: ")
        numero2 = ler_numero("Digite o segundo número: ")

        try:
            resultado = calcular(operacao, numero1, numero2)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Programa encerrado.")  
            break


if __name__ == "__main__":
    main()