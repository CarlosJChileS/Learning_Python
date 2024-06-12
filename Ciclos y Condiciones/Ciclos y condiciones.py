#none part 1

#cuando no hay ni un valor
resultado = None

print(resultado)

#none es un valor falso
#True(1) / false(0)

#formas de demostar un valor falso
"""
False
none
0
.0
'' / ""
[]
()
{}
"""
#Condiciones part2
#if
resultado =11

resultado= resultado>10

#imprime si se cumple
if resultado > 19 and resultado <20:
    print('la variable cumple la condicion ')
#si no se cumple
else:
    print('la condicion no se cumple')

#multiples condiciones part3
#elif

calificacion = 8

if calificacion == 10:
    print("calificacion perfecta")
elif calificacion == 9 or calificacion ==8 or calificacion ==7 :
    print("aprobaste la materia")
else:
    print("no pasaste")

#ternario part4
"""    
calificacion1= 10
color = None

if calificacion >=7:
    color = "verde"
else:
    color= "rojo"

print(calificacion1, color)"""

#ternario 

calificacion1= 10
color= 'verde' if calificacion >= 7 else "rojo"


print(calificacion1, color)

#Asignar valores mediante operadores lógicos part5

variable= 'Carlos' or 'Junior'

print(variable)
#python reconoce el valor simepre primero el de la izquierda

#While part 6
contador =1

while contador <=10:
    print(contador)

    contador= contador+1
    #se ejecutara hasta que llegue al valor 10
    # se ejecuta hasta la condicion se cumple

numero = 1234
contador_digitos = 0

while numero >=1:
    #contador_digitos = contador_digitos +1
    contador_digitos +=1

    numero = numero/10
#crear else es opcional
else:
    print('fin del ciclo while')

print(contador_digitos)

#For part7 

usuarios = ['usuario1','usuario2','usuario3','usuario4']

#imprime cada uno de los elementos
for ususarios in usuarios:
    print(usuarios)

#break part8

titulo_curso= 'Python'

for caracter in titulo_curso:
    
    if caracter == 'h':
        break #finaliza el ciclo
    #continue pasa a la siguiente interaccion

print(titulo_curso)

    

