#Variables part 1
#Se utiliza el # para comentar  cuando es una linea
"""
se utiliza mas cuando son varias lineas

"""

#Variables

titulo_tema= 'my python learning'
nombre_completo = 'carlos junior chile silva'

#Para mostrar mensaje en el terminal
print(titulo_tema)
print(nombre_completo)

#Existen tipos de datos:

# string texto
titulo_tema= 'my python learning'

# Int numeros enteros positivos o negrativos
numero_uno = 10 //3 #al divididir con doble # es tipo de dato entero

# Float numero decimal
numero_dos = 3.14


# Bool solo verdadero o falso 
#True or False
valor = True

#Para saber el tipo de variable se utiliza  type

print(type(numero_uno))

#si una misma variable tiene lo mismo se quedara con lo ultimo

valor = "Carlos"
valor = 2
print(valor) #imprimiria el valor de 2

#Los signos de relacion son los siguientes
""""
    <
    >
    >=
    ==
    !=
"""
numero_uno =10
numero_dos =20


resulto = numero_uno == numero_dos
print(resulto)

#CONSTANTES PART 2

nombre_completo = input("Ingresa tu nombre completo: ")

print(nombre_completo)
print(type(nombre_completo))

edad = int(input('Ingresa tu edad:'))


altura =float(input("ingrese tu altura"))

print(edad)
print(type(edad))

autorizacion = input("autorizas el programa(si/no)" ) == 'si'

print(autorizacion)

#PART 3
#OPERADORES LOGICOS
numero_uno =10
numero_dos =20

#and, or y not
#true and False

resultado_numeros= numero_uno > numero_dos

print(resultado_numeros)

#PART 4
#PALABRAS RESERVADAS
"""Aquí el listado de todas ellas:

 	 	 	 
False	class	is	return
None	continue	lambda	try
True	def	nonlocal	while
and	del	not	with
as	elif	or	yield
assert	else	pass	*
break	except	raise	*"""