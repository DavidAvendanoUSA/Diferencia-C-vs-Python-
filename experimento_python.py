import random 
 
# num_elementos = int(input("numero de elementos a reganizar: "))
num_elementos = 10000
list = [random.randint(1,100) for i in range (num_elementos)]

longitud = len(list)

#print(list)

for i in range(longitud-1):
	for j in range(longitud-i-1): 
		if list[j] > list[j+1]: 
			temp = list[j]
			list[j] = list[j+1]
			list[j+1] = temp

#print(list)

