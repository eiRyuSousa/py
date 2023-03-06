num = input("Digite um número inteiro de três dígitos: ")

if len(num) != 3:
    print("Número inválido")
else:
    digito1 = int(num[0])
    digito2 = int(num[1])
    digito3 = int(num[2])
    soma = digito1 + digito2 + digito3
    print("A soma dos dígitos é:", soma)
