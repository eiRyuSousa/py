idade = int(input("Qual a sua idade? "))
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))

anos_fumando = idade * 365
total_cigarros = anos_fumando * cigarros_por_dia
dias_perdidos = total_cigarros * 10 / 1440

print("Você já perdeu aproximadamente {0:.2f} dias de vida devido ao hábito de fumar.".format(dias_perdidos))
