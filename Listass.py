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

