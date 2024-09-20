a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))
d = float(input("Digite o coeficiente D: "))
e = float(input("Digite o coeficiente E: "))
f = float(input("Digite o coeficiente F: "))

x = ((c * e) - (b*f))/((a*e) - (b*d))
y = ((a*f) - (c*d))/((a*e)- (b*d))

print(x)
print(y)