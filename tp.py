#dnis
dni1 = "39115153"
dni2 = "37125154"
dni3 = "38115158"
dni4 = "34116164"

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

print(conjunto1,conjunto2,conjunto3,conjunto4)

#operaciones
