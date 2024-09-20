
for i in range(4):
  print("assign M"+"["+str(i)+"]"+ "= (~S & X"+"["+str(i)+"]) | (S & Y["+str(i)+"]);")


for i in range(4):
  print("X["+str(i)+"] = sw"+str(i+1)+";")

for i in range(4):
  print("Y["+str(i)+"] = sw"+str(i+5)+";")

for i in range(4):
  print("M["+str(i)+"] = led"+str(i)+";")


for i in range(2):
  print("assign Z"+"["+str(i)+"]"+ "= (~S & U"+"["+str(i)+"]) | (S & V["+str(i)+"]);")