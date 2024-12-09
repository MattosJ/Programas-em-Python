import statistics
lista = [12,15,28,56,78,78,80]
somaDaLIsta = sum(lista)
media = somaDaLIsta/len(lista)
print(media)

mediaComStatic = statistics.mean(lista)

mediana = statistics.median(lista)
print(mediana)

moda = statistics.mode(lista)

print(moda)