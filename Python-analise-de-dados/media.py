def media():
    somatorio = 0
    nElementos = int(input("Digite o número de elementos: "))
    lista = []
    for i in range(nElementos):
        dado = float(input(""))
        lista.append(dado)
        somatorio += dado
    media = somatorio / nElementos
    return media

def main():
  resultado = media()
  print(resultado)

if __name__ == "__main__":
    main()