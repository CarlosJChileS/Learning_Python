
#diccionarios
"""elementos = {'a': 1,'b': 2, 'c':3, 'a': 4}
#el valor de la llave el ultimo valor asignado

"""
"""#agregar elementos
elementos['nombre'] = 'Cody'#crea la llave
elementos[(1,2,3)] = 'la llave es una tupla'

#modificar valor
elementos['nombre'] = 'Codidgofacilito'#actualiza la llave
"""
"""print(elementos)"""

#obtener elementos
diccionario = {'a': 1,'b': 2, 'c':3, 'd': 4}
"""
print('a' in diccionario)
valor = diccionario['d']
print(valor)"""

#get en diccionario valor de una llave en forma segura osea que exista
valor= diccionario.get('d')
#valor= diccionario.get('z', 'la llave no existe en el diccionario')
#se puede poner cualquier tipo de valor

#setdefault en caso de que la llave no exista se agregara al dicionario
valor =diccionario.setdefault('e',5)

print(valor)
print(diccionario)

#PART 2
#LLAVES, ITEMS Y VALORES
diccionario = {'a':1, 'b': 2,'c':3, 'd':4}

#keys
#values
# items

#retornara lo que se encuentra almacenado en las llavees
llaves = tuple(diccionario.keys())
print(llaves)

#obterner valores
valores = diccionario.values()
print(valores)

elementos= tuple(diccionario.items())
print(elementos)
#formas de conocer los elementos de un diccionario

#PART 3
#ELIMINAR ELEMENTOS DEL DICCIONARIO
diccionario = {'a':1, 'b': 2,'c':3, 'd':4}


#1era forma es del
#pop 

#longitud del diccionario
print(len(diccionario))

#si no existe la llave saldra error
del diccionario['a'] #1 
#del se usa para eliminar

valor = diccionario.pop('b') #eliminar 2

#clear para eliminar todos los elementos del diccionario
#diccionario.clear()


print(diccionario)
print(len(diccionario))

