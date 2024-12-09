stringQualquer = 'Olá Mundo!'
print(stringQualquer)
print(len(stringQualquer))
print(type(stringQualquer))
print(stringQualquer + ' Concatenei!')
print(stringQualquer.replace('Mundo!','James'))
CPF = 'CPF:123456789'
print(int(CPF.replace('CPF:','')))
print(stringQualquer.startswith('Olá'))
print(stringQualquer.endswith('Mundo!'))
print(stringQualquer.count('M'))
string = 'Eu estou testando quantas vezes aparece o e.'
print(string.count('e'))
nome = 'james'

print(nome.capitalize())
cpf = '123456789'
print(cpf.isdigit())
print(stringQualquer.isalnum())
print(nome.upper())
print(nome.lower())

frase = 'Hoje o dia está calor'

print(frase.find('calor'))

endereco = 'Rua 9 número 66.'

print(endereco.strip())

palavra = 'Rua Augusta 150, Centro, SP'

print(palavra.split(','))
