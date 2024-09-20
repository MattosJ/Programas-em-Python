 ###Crie uma função que mostra na tela os primeiros 10 números naturais usando recursão.
###Por exemplo: 1 2 3 4 5 6 7 8 9 10

def imprimirUsandoRercusao(n = 1):
  if n <= 10:
    print(n)
    return imprimirUsandoRercusao(n+1)
  else:
    exit()
imprimirUsandoRercusao()