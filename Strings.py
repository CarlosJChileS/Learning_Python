
#split nos permite generar una lista apartir de una lista
#join lo contrario
#split
"""
lenguajes = 'python ruby java rust c++ c'


listado_lenguajes = lenguajes.split()#lo divide por el espacio
#listado_lenguajes = lenguajes.split(-) en el guion va el signo que se quiere dividir
#listado_lenguajes = lenguajes.split(-, 2) ahi se dividira 2 veces
 
print(listado_lenguajes)
"""
#join 
lenguajes = ['python ruby java rust c++ c']

string_lenguajes = ' '.join(lenguajes)#utliza el caracter dentro del ' '

print(string_lenguajes)
print( type(string_lenguajes))


#PART 2
#CONCATENAR

#concatenar pt1
"""nombre = 'Carlos Junior'
apellido= 'Chile'

#nombre_completo = 'mr.' + nombre +' '+ apellido
#se concatena usando el + 

nombre_completo = 'Mr/ %s %s.' %(nombre, apellido)
#los %s son reemplazado por los valores

print(nombre_completo)"""

nombre = 'Carlos Junior'
apellido= 'Chile'

#nombre_completo = 'Mr. {} {} {}.{} '.format(nombre, apellido, 'perez')
#                       es opcional nombrarlos

#aqui en modo clase
"""nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.{} '.format(
    nombre= nombre,
    primer_apelido= apellido
    segundo_apellido= 'perez')
print(nombre_completo)

"""