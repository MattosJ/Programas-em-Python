def media_quantidade_definida():
 quantosDados = int(input('Quantos dados você tem : '))
 somatorio = 0
 for i in range(quantosDados):
  dado = float(input("Digite o dado: "))
  somatorio += dado
 media = somatorio / quantosDados
 print(media)
 return main()


def media_quantidade_indefinida_com_while():
 somatorio2 = 0
 i = 0
 r = "S"
 while r == "S" :
  dado = float(input('Digite o dado: '))
  somatorio2 += dado
  i += 1
  r =  input('S para continuar , N para encerrar e ver a média: ').upper()
  
  
  media2 = somatorio2 / i
 print(media2)
 return main()

def media_quantidade_indefinida_com_lista():
  notas = []
  continuar = "S"
  while continuar == "S" :
   nota = float(input('Digite a nota: '))
   notas.append(nota)
   continuar = (input("Quer continuar? Sim - S , Não - N : ")).upper()
  somaNotas = sum(notas)
  tamanhoDaLista = len(notas)
  mediaComLista = somaNotas / tamanhoDaLista
  print(mediaComLista)
  return main()
 
def main():
 fica = 0
 print("Se quiser Calcular a média sabendo a quantidade de nota digite 1")
 print("Se quiser Calcular a média sem saber a quantidade de notas com while e sem lista digite 2")
 print("Se quiser Calcular a média sem saber a quantidade de notas com while e  lista digite 3")
 print("Se quiser encerrar o programa digite 4")
 fica = int(input("O que deseja fazer: "))
 if fica == 1:
  media_quantidade_definida()
 if fica == 2:
  media_quantidade_indefinida_com_while()
 if fica == 3:
  media_quantidade_indefinida_com_lista()
 else:
  exit()
main()