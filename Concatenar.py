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