
#Declarare lista
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#Afisare lista ordonata ascendent
lista_ascendent = my_list.copy()
lista_ascendent.sort()
print("Lista ordonata ascendent:", lista_ascendent)

#Afisare lista ordonata descendent
lista_ascendent.reverse()
print("Lista ordonata descendent:", lista_ascendent)

#Afisarea numerelor cu indici pari din lista
my_sliced_list = my_list[::2]
print("Numerele cu indici pari sunt:", my_sliced_list)

#Afisarea numerelor cu indici impar din lista
my_sliced_list = my_list[1::2]
print("Numerele cu indici impari sunt:", my_sliced_list)

#Afisarea elementelor multipli ai lui 3
multiplii = [x for x in my_list if x % 3 == 0]
print("Elementele multipli ai lui 3:", multiplii)