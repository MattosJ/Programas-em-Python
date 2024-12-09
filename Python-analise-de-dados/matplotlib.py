import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)

y = np.random.randint(low = 1, high = 1500, size = 10)

y

plt.plot(y)

plt.plot(y,color = '#749187' , marker = 'o', ms = 5, mec = 'k', markerfacecolor = 'w', ls = '-.')

plt.plot(y*2, marker = '+', color = 'k', ms = 5)

plt.xlabel('Eixo X', color = 'red', size = 12)
plt.ylabel('Eixo Y')
plt.title('Título', loc = 'left')

plt.grid(axis = 'y', color = 'gray', linestyle = '--', linewidth = 1, alpha = 0.80)
plt.show()

np.random.seed(6)
x = np.arange(1,11)
y1 = np.random.randint(1,400,10)
y2 = np.random.randint(150,500,10)
y3 = np.random.randint(200,600,10)

plt.figure(figsize = (15, 5))
plt.suptitle('Figura', fontsize = 15)

plt.suptitle('figura', fontsize = 15)

plt.subplot(1,3,1)
plt.plot(x,y1, color = 'k')
plt.title('subplot 1', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1,3,2)
plt.plot(x,y2, color ='r')
plt.title('Subplot 2', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1,3,3)
plt.plot(x,y3, color = 'g')
plt.title('Subplot 3', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.tight_layout(pad = 4)
plt.show()

fig, ax = plt.subplots(1,3, figsize = (15,5))
fig.suptitle('Figure')
ax[0].plot(x, y1, color = 'black')
ax[1].plot(x,y2, color = 'red')
ax[2].plot(x , y3, color = 'green')

for i in range(3):
  ax[i].set(title = f'subplot {i+1}', xlabel = 'Eixo X', ylabel = 'Eixo Y')