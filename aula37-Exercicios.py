#Fibonacci
#1, 1, 2, 3, 5, 8 ...

#fibonacci(5) = fibonacci(4) + fibinacci(3) = 3 + 2 = 5
#
#fibinacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
#fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
#
#fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
def fibonacci(pos):
    if pos == 1 or pos == 2:
        return 1
    return fibonacci(pos-1) + fibonacci(pos-2)

#Potencia
def pot(base, expo):
    if expo == 0:
        return 1
    return base * pot(base, expo-1)

#Verificar se número é par
def eh_par(num):
    return num%2==0

#verificar se número é primo (1 não é primo)
def eh_primo(num):
    if num == 1:
        return False

    for div in range(2, int(num/2)+1):
        if num%div == 0:
            return False
    return True

#Versão do professor:
def eh_primo_prof(num):
    div = 0
    for i in range(1, num+1):
        if num % i == 0:
            div += div
    return False if div > 2 else True

'''
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
'''
'''
print(pot(2, 2))
print(pot(3, 4))
print(pot(2, 0))
print(pot(2, 1))
'''
'''
print(eh_par(2))
print(eh_par(3))
print(eh_par(444))
print(eh_par(123))
print(eh_par(0))
'''
'''
print(eh_primo(1))
print(eh_primo(2))
print(eh_primo(3))
print(eh_primo(4))
print(eh_primo(5))
print(eh_primo(6))
print(eh_primo(7))
print(eh_primo(10))
print(eh_primo(13))
print(eh_primo(121))
print(eh_primo(11))
'''


'''
var1 = 3.141516
var2 = 7
var3 = "oi"

print('String {0:.3f}, foat {1:10d}, int {2:10}.'.format(var1, var2, var3))
'''