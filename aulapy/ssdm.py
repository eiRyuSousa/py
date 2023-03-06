# solicita que o usuário insira dois números inteiros
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# solicita que o usuário escolha a operação desejada
operacao = input("Escolha a operação desejada (+, -, * ou /): ")

# verifica se a operação escolhida é válida
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    resultado = None

# exibe o resultado
if resultado is not None:
    print("Resultado:", resultado)
