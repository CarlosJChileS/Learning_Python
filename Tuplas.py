"""las tuplas son inmutables
tupla = ('string', 10,15.4, True,[1,2,3])


print(tupla)
print(type(tupla))"""

cursos = ('python', 'flask,', 'django' , 'rails', 'mongodb')

primer_curso = cursos[0]
print(primer_curso)

#subtupla
sub_tupla = cursos[0:3]
print(sub_tupla)

#lista es corchetes

#tuplas es parentesis

#crear tupla a partir de lista

cursos2 = ['python', 'django', 'flask']
cursos_tupla = tuple(cursos2)
print(cursos_tupla)

#crear lista a partir de tupla
niveles = ('basico','intermedio', 'avanzado')

niveles_lista=list(niveles)

print(niveles_lista)
print(type(niveles_lista))

#PART 2
#DESCOMPRIMIR

numeros= (1, 2, 3, 4, 5, 6, 7, 8)
uno, dos, tres, cuatro, *resto_valores = numeros
#el aterisco denota lista *
# _ omitir lista
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

#PART 3 COMPRIMIR
lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista2 = [100, 200, 300, 400, 500]
resultado = zip(lista, tupla,lista2)# zip
print(resultado)

resultado = tupla(resultado)
print(resultado)

