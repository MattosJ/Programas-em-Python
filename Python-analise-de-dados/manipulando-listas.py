lista = []
print(lista)

lista.append(1)
print(lista)
lista.append(4)
print(lista)
print(len(lista))
print(lista[0])

lista.clear()
print(lista)

lista.insert(0,8)
print(lista)
lista.insert(1,4)
print(lista)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)
print(lista1)

lista1.remove(5)
print(lista1)

lista1.pop(0)
print(lista1)

listaABC = ['z','c','f','h','a']
listaABC.sort()
print(listaABC)

listaABC.sort(reverse=True)
print(listaABC)

listaNova = listaABC.copy()
print(listaNova)

print(listaNova.index('a'))