# Exibe uma arte ASCII de uma ilha do tesouro
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Exibe uma mensagem de boas-vindas ao jogo
print("Welcome to Treasure Island.")
# Informa ao jogador sobre a missão
print("Your mission is to find the treasure.") 

# Solicita ao usuário que escolha um caminho na encruzilhada, convertendo a resposta para minúsculas
answer = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()

# Verifica se a escolha foi "left"
if answer == 'left':
  # Se o jogador escolheu "left", pergunta sobre a próxima ação no lago
  answer2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
  # Verifica se a escolha foi "wait"
  if answer2 == 'wait':
    # Se o jogador escolheu "wait", pergunta sobre a cor da porta
    answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    # Verifica se a escolha foi "red"
    if answer3 == 'red':
      print("Burned by fire. Game Over.")
    # Verifica se a escolha foi "yellow"
    elif answer3 == 'yellow':
      print("You Win!")
    # Verifica se a escolha foi "blue"
    elif answer3 == 'blue':
      print("Eaten by beasts. Game Over.")
    # Se a escolha não foi nenhuma das opções válidas
    else:
      print("Game Over.")
  # Se a escolha no lago não foi "wait"
  else:
    print("Attacked by trout. Game Over")
# Se a escolha na encruzilhada não foi "left"
else:
  print("Fall into a hole. Game Over")
