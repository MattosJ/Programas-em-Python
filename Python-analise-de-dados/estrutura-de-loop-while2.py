import random
while True:
  eu = random.randint(0,10)
  voces = random.randint(0,10)

  print('Eu tirei o valor: ',eu)
  print('Vocês tiraram o valor: ', voces)

  if eu > voces:
    print('Venci!!')
    break
  print('\n')