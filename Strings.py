
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