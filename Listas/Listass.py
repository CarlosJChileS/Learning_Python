
#PART 1
#nos permiten manejar grandes datos
lista = list()
lista2= []
#cualquiera de las dos formas crear lista
#la posicion de la lista se llama indice
lista_cursos = ['python','django','flask','ruby','java']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)
#actualizar elemento

lista_cursos[4]='rust'#para actualizar elemento
print(lista_cursos)
#sublistas
# [STAR: END]
#[STAR:] OBTENEMOS LOS ULTIMOS ELEMENTOS DE LA LISTA
#[ :END] HASTA EL INDICE QUE SALE, LOS PRIMEROS
#[STAR:END: SALTOS2] SALTOS DE 2 EN DOS
# [:] SUBLISTA CON TODOS LOS ELEMENTOS
#[::2]SALTO DE 2 EN DOS
#[::-1]INVERTIR LA LISTA
sub_lista = lista_cursos[0:3]
print(sub_lista)

##MODIFICAR LISTAS
lista_cursos = ['python','django','flask','ruby','java']
lista_cursos_2 = ['c','c++','docker']
lista_cursos.append('mongodb')#anadir eleemtno


lista_cursos.insert(1, 'rails')
#anadir en el indice numero 1

lista_cursos.extend(lista_cursos_2)
#anadir la segunda lista 

lista_cursos.remove('mongodb')
#para eliminar el elemento
print(lista_cursos)

del lista[0]
#eliminar con indice
print(lista_cursos)


lista_cursos.clear()
#la lista va a quedar vacia

#PART 2
#MODIFICAR LISTAS
lista = [8, 90, 1 ,5, 44, 132, 600, 3, 4]

lista.sort()
#ordenar lista de menor a mayor

print(lista)

lista.sort(reverse=True)
#ordenar de mayor a menor
print(lista)

#min - max
print(min(lista))
print(max(lista))

#para ver si se encuentra o no en la lista
10 in lista

print(5 in lista)
print(11 not in lista)
#para conocer el indice donde se encuentra el elemento
#retorna solo el primer indice
index= lista.index(5)
print(index)

#PART 3
#MATRICES

columna_a = [10,20,30,40]
columna_b = [30,40,50,60]

matriz = [columna_a, columna_b] #es una matriz 2 x 4

print(matriz)
print(matriz[0][0])# para elegir el valor especifico