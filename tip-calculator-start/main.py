# Exibe uma mensagem de boas-vindas ao usuário
print("Welcome to the tip calculator!")

# Solicita ao usuário o valor total da conta e o converte para um número de ponto flutuante
bill = float(input("What was the total bill? $"))

# Solicita ao usuário a porcentagem de gorjeta que ele deseja dar (10, 12 ou 15) e a converte para um inteiro
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Solicita ao usuário o número de pessoas para dividir a conta e o converte para um inteiro
people = int(input("How many people to split the bill? "))

# Calcula o valor da gorjeta como uma porcentagem do valor total da conta
percent = bill * tip / 100

# Calcula o valor total da conta incluindo a gorjeta e divide pelo número de pessoas
total = (percent + bill) / people

# Exibe a quantia que cada pessoa deve pagar, arredondando para duas casas decimais
print(f"Each person should pay: ${round(total, 2)}")