#para crear las clases se usa la palabra
#class
class Usuario:
    pass

carlos = Usuario()
print(carlos)

#2
#ATRIBUTOS DE CLASE
#los atributos le pertenecen a una clase y
# SE DIVIDEN EN 2 TIPOS: DE CLASE Y DE INSTANCIA

class Usuario:
    #atrs de clase
    username = 'username por default'
    email = ''


#para modificar valor
Usuario.username= 'user1'
Usuario.email= 'carlos@gmail.com'
print(Usuario.username)

#3
#ATRIBUTOS DE INSTANCIA

class Usuario:
    #atrs de clase
    username = 'username por default'
    email = ''

#__dict__
    

user1= Usuario()
"""
#1 verifica si el attr existen dentro del objeto
#2 verifica si el attr existe dentro de la clase para lectura
#3 lanza un error"""


print(user1.username) 

print(user1.__dict__) # dict para conocer los attr

#3
#ATRIBUTOS DINAMICOS

class Usuario:
    #atrs de clase
    username = 'username por default'
    email = ''

#__dict__
    

user1= Usuario()
user2= Usuario()
"""
#1 verifica si el attr existen dentro del objeto
#2 verifica si el attr existe dentro de la clase para lectura
#3 lanza un error"""

user1.username= 'carlos' # agregamos el atributo
user1.password= '1234'

print(user1.username) #de instancia

print(user1.__dict__) # dict para conocer los attr

print(user2.__dict__)

#4
#METODOS
#__init__

#ya no se utilizara esTO
class Usuario:

    def inicializar(self, username, password):
        self.username = username
        self.pasword= password

user1 = Usuario()
user2 = Usuario()

user1.inicializar('user1','password1') # se agregan los atributos al objeto
user2.inicializar('user2','password2') # se agregan los atributos al objeto


print(user1.__dict__)
print(user2.__dict__)

#5 
#METODO INIT

class Usuario:

    #objet
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

        

user1 = Usuario('user1','password1')
user2 = Usuario('user2','password2')
user3= Usuario('user3','password3')#establecen valores

user4= Usuario()

print(user1.__dict__) #dict es diccionario
print(user2.__dict__)
print(user3.__dict__)

#6
#Herencia

class Mascota: #clase padre
    
    def comer(self):
        print('la mascoa come')

    def dormir(self):
        print('la mascota duerme')


class Perro(Mascota): #clase hija
    pass

class Gato(Mascota):
    pass


duke = Perro()

duke.comer()
duke.dormir()

Paco= Gato()

Paco.comer()
Paco.dormir()

#7
#HERENCIA MULTIPLE

class Animal(): #clase padre
    
    def comer(self):
        print('la mascoa come')
    
    def dormir(self):
        print('la mascota duerme')




class Mascota(Animal): # clase padre
     pass
    


class Felino: #clase hija

    def cazar(self):
        print('el felino caza ratas')


class Gato(Mascota,Felino): # clase hija
    pass


paco= Gato

paco.comer()
paco.dormir()
paco.cazar()

#8
#SOBREESCRITURA DE METODOS

class SerVivo:

    def dormir(self):
        print('el ser duerme')



class Animal(SerVivo): #clase padre
    
    def comer(self):
        print('el animal come')
    
    def dormir(self):
        print('el animal duerme')




class Mascota(Animal): # clase padre
     def comer(self):
        print('la mascota come')
    


class Felino: #clase hija

    def cazar(self):
        print('el felino caza ratas')


class Gato(Mascota,Felino): # clase hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come')

    def dormir(self):
        print(f'{self.dormir} duerme')

paco= Gato('patricio')

paco.comer()
paco.dormir()
paco.cazar()

#9
#SOBRE ESCRITURA DE METODOS PT2

#METODO SUPERpara imprimir lo anterior

class SerVivo:

    def dormir(self):
        print('el ser duerme')



class Animal(SerVivo): #clase padre
    
    def comer(self):
        print('el animal come')
    
    def dormir(self):
        print('el animal duerme')




class Mascota(Animal): # clase padre
     def comer(self):
        super().comer()
        print('la mascota come')
    


class Felino: #clase hija

    def cazar(self):
        print('el felino caza ratas')


class Gato(Mascota,Felino): # clase hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come')

    def dormir(self):
        print(f'{self.dormir} duerme')

paco= Gato('patricio')

paco.comer()

#10
#METODOS DE CLASE

class Circulo:

    pi = 3.141592

    @classmethod#para crear clase se usa este decorador
    def area(cls,radio): #hacer referencia a la clase cls
        return cls.pi *(radio** 2)
    
resultado = Circulo.area(14)
print(resultado)




