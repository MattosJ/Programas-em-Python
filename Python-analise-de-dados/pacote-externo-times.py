import time
print('Comecei agora...')
time.sleep(3)
print('Terminei')
agora = time.localtime()
print(agora)
print(type(agora))

print(time.strftime('%d/%m/%y , %H:%M:%S', agora))

time_texto ='21 june, 2021'
print(time.strptime(time_texto, '%d %B, %Y'))