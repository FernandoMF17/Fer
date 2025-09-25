lista = [1,4,5,6,4.3,"Fernando", True]
#print(lista)
lista[6] = "Hola"
#print(lista)

tupla = (1,4,5,6,4.3,"Fernando", True)
#print(tupla)

datos_personales = {'Fernando': '51', 'Luis' : 70, 'Cris':60, 'Ana': 20, 'Maria': 30, 'Roger': 100}
#datos_personales['direccion'] = 'San Francisco' 
#datos_personales.update({'correo': 'fmoralesflores0@gmnail.com'})
print(datos_personales)

def suma(a,b):
    sum = a + b
    return sum

resultado = suma (10,5)
print(resultado)

def impares(n):
    if (n % 2 == 1):
        return n

lista = [1,2,3,4,5,6,7,8,9,10]
lista_impares = filter(impares, lista)
print(list(lista_impares))

a = 5