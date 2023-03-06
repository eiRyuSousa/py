num = int(input("Digite um número inteiro: "))
soma = 0
temp = num
while temp > 0:
   digito = temp % 10
   soma += digito ** 3
   temp //= 10
if num == soma:
   print(num,"é um número de Armstrong")
else:
   print(num,"não é um número de Armstrong")
