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