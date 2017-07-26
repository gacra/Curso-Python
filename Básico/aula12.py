var = True
print(type(var))
var = not var
#Basta digitar var, p/ imprimir no IDLE
print(var)
var = not var
print(var)

v1 = True
v2 = False
v3 = True
v4 = False

r1 = v1 and v2
r2 = v1 and v3
r3 = v1 or v2
r4 = v2 or v4

print(r1)
print(r2)
print(r3)
print(r4)
print(not r1)