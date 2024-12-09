lista = ['Brasil','Argentina','Uruguai','Paraguai','Bolivia','Colombia','Equador']
for i in lista:
  print(i)
  print(i[0:2])
for i in lista:
  if i == 'Uruguai':
    print(i, 'É Bicampeão Mundial!')
  elif i == 'Brasil':
    print(i, 'É Penta campeão Mundial!')
  elif i == 'Argentina':
    print(i, 'É Tricampeão Mundial')
  else:
    print(i, 'Não é campeão Mundial') 
for i in range(0,len(lista),2):
  print(lista[i])