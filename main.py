from funciones import  *

dni1 = "39115153"
dni2 = "12345567"
dni3 = "89702134"
dni4 = "12345678"

"""
dni1 = input("Ingrese su dni: ")
dni2 = input("Ingrese su dni: ")
dni3 = input("Ingrese su dni: ")
dni4 = input("Ingrese su dni: ")
"""

conjunto1 = digitos_unicos(dni1)
conjunto2 = digitos_unicos(dni2)
conjunto3 = digitos_unicos(dni3)
conjunto4 = digitos_unicos(dni4)

#print(conjunto1,conjunto2,conjunto3,conjunto4)
#print(union(conjunto1,conjunto2,conjunto3,conjunto4))
#print(interseccion(conjunto1,conjunto2,conjunto3,conjunto4))
#print(diferencia_entre_pares(conjunto1,conjunto2,conjunto3,conjunto4))
#print(diferencia_simetrica(conjunto1,conjunto2,conjunto3,conjunto4))