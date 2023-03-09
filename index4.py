# ordem decrescente

andares = 20

print("O dono do hotel é supersticioso, não temos o 13º andar!")
print() 

for contador in range(andares,0,-1):
  if contador == 13:
    continue
  print(f"{contador}º andar")