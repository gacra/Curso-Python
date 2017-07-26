'''
Fatorial
0! = 1
1! = 1
2! = 2*1=2
3! = 3*2*1=6
4! = $*3*2*1=24
'''

def fat(n):

    if n==0:
        return 1;

    return n*fat(n-1)

print(fat(0))
print(fat(3))
print(fat(4))
print(fat(5))