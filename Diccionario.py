
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