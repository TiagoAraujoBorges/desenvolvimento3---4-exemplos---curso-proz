# laço while

andares = 20
contador = 1

print("O dono do hotel é supersticioso, não temos o 13º andar!")
print()

while (contador <= andares):
  print(f"{contador}º andar") 
  contador = contador + 1
  if contador == 13:
    contador = contador + 1

