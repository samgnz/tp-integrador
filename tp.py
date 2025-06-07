#dnis
dni1 = "39115153"
dni2 = "12345567"
dni3 = "89702134"
dni4 = "12345678"

def digitos_unicos(dni):
    digitos_unicos = []
    
    for digito in dni:
        digito = int(digito)
        if digito not in digitos_unicos:
            digitos_unicos.append(digito)
    return digitos_unicos


conjunto1 = digitos_unicos(dni1)
conjunto2 = digitos_unicos(dni2)
conjunto3 = digitos_unicos(dni3)
conjunto4 = digitos_unicos(dni4)



#operaciones
def union(dni1,dni2,dni3,dni4):
    DNIS= dni1+dni2+dni3+dni4
    union = []
    
    for digito in DNIS:
        digito = int(digito)
        if digito not in union:
            union.append(digito)
    return union


def interseccion(dni1,dni2,dni3,dni4):
    dni1_lista= list(map(int, dni1))
    dni2_lista= list(map(int, dni2))
    dni3_lista= list(map(int, dni3))
    dni4_lista= list(map(int, dni4))
    
    interseccion = []

    for digito in dni1_lista:
        if digito in dni2_lista and digito in dni3_lista and digito in dni4_lista:
            if digito not in interseccion:
                interseccion.append(digito)
    return interseccion


def diferencia_entre_pares(dni1,dni2,dni3,dni4):
    dni1_lista= list(map(int, dni1))
    dni2_lista= list(map(int, dni2))
    dni3_lista= list(map(int, dni3))
    dni4_lista= list(map(int, dni4))
    
    diferencia = []

    for digito in dni1_lista:
        if digito not in dni2_lista and digito not in dni3_lista and digito not in dni4_lista:
            if digito not in diferencia:
                diferencia.append(digito)
    return diferencia


def diferencia_simetrica(dni1,dni2,dni3,dni4):
    dni1_lista= list(map(int, dni1))
    dni2_lista= list(map(int, dni2))
    dni3_lista= list(map(int, dni3))
    dni4_lista= list(map(int, dni4))
    
    diferencia = digitos_unicos(dni1_lista)

    for digito in dni1_lista:
        if digito in dni2_lista or digito in dni3_lista or digito in dni4_lista:
            if digito in diferencia:
                diferencia.remove(digito)
    return diferencia


#frecuencia

def frecuencia_por_digito(dni):
    frecuencia = {}
    
    numeros = list(map(int, dni))

    for digito in numeros:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

#print(frecuencia_por_digito(dni1))
#print(frecuencia_por_digito(dni2))
#print(frecuencia_por_digito(dni3))
#print(frecuencia_por_digito(dni4))


#suma todos los digitos
def suma(dni1,dni2,dni3,dni4):
    DNIS= dni1+dni2+dni3+dni4

    numeros = list(map(int, DNIS))
    suma_total= 0
    for digito in numeros:
        suma_total= digito + suma_total
    return suma_total

#print(suma(dni1,dni2,dni3,dni4))


#evaluacion de condiciones logicas
#diversidad total
def diversidad_total(dni1,dni2,dni3,dni4):
    DNIS= dni1+dni2+dni3+dni4
    diversidad = []
    
    for digito in DNIS:
        digito = int(digito)
        if digito not in diversidad:
            diversidad.append(digito)
    print(diversidad)        
    if len(diversidad) == 10:
        print("Se alcanza la diversidad total")
    else:
        print("No alcanza la diversidad total")
    
    return diversidad 

#diversidad_total(dni1,dni2,dni3,dni4)

#diversidad numerica
def diversidad_numerica(dni1, dni2, dni3, dni4):
    conjunto_dni1 = digitos_unicos(dni1)
    conjunto_dni2 = digitos_unicos(dni2)
    conjunto_dni3 = digitos_unicos(dni3)
    conjunto_dni4 = digitos_unicos(dni4)
    
    conjuntos = [conjunto_dni1, conjunto_dni2, conjunto_dni3, conjunto_dni4]

    baja = 0
    alta = 0

    for conjunto in conjuntos:
        if len(conjunto) < 5:
            baja += 1
        else:
            alta += 1

    if alta < baja:
        print("Hay una baja diversidad numérica")
    elif baja == alta:
        print("Hay una diversidad numérica equilibrada")
    else:
        print("Hay una alta diversidad numérica")
    
diversidad_numerica(dni1,dni2,dni3,dni4)



