class Pessoa:
  def __init__(self,Nome,Idade):
    self.Nome = Nome
    self.Idade = Idade

  def Boas_Vindas(self):
    print('Olá seja bem-vindo: ',self.Nome)

  def Recusado(self):
    print("Seu acesso foi negado!")

  def Maior_Idade(self):
    if self.Idade >= 18:
      print('Usuário é maior de Idade!')
      self.Boas_Vindas()
    else:
      print('O usuário é menor de idade!')
      self.Recusado()
dados = Pessoa('James', 20)
print(dados.Maior_Idade())