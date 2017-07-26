'''
import my_math

print(my_math.media(2, 4))
print(my_math.somar(2, 4))
'''

#Para não precisar digitar my_math sempre que usar uma função
#Fazemos um import universal
#Entretanto, esse tipo de import não é recomendável, pois pode ser perigoso importar td de um módulo
from my_math import *

print(media(2, 4))
print(somar(2, 4))