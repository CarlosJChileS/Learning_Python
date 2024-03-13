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
