import datetime
diaHoje = datetime.datetime.today()
print(diaHoje)

print(type(diaHoje))

variavel = datetime.datetime.today().date()
print(variavel)

data = datetime.datetime.today().date()
ano = data.year
mes = data.month
dia = data.day

print(ano)
print(mes)
print(dia)

dataAntiga = datetime.date(2023,8,23)
print(dataAntiga)

print(data - dataAntiga)

print(data.strftime('%d/%m/%y'))

print(data + datetime.timedelta(days=12))
