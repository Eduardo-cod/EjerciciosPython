motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati") #agrego ducati al final de la lista
print(motorcycles)

motorcycles[0] = "ducati" #remplazo honda por ducati
print(motorcycles)

motorcycles.insert(0, "harley") #inserto harley al inicio de la lista
print(motorcycles)

del motorcycles[0] #elimino el primer elemento de la lista
print(motorcycles)

popped_motorcycle = motorcycles.pop() #elimino el ultimo elemento de la lista y lo guardo en una variable
print(motorcycles)
print(popped_motorcycle) #imprimo la variable que contiene el ultimo elemento eliminado

motorcycles.remove("suzuki") #elimino un elemento especifico de la lista
print(motorcycles)

'''
#imprimo el elemento que se encuentra en la posicion 3 de la lista
print(motorcycles[3]) #ocasiona un error porque la lista tiene solo 3 elementos y el indice 3 no existe.
'''

print(motorcycles[-1]) #imprimo el ultimo elemento de la lista usando un indice negativo

'''
#ocasiona un error porque la lista esta vacia y no hay ningun elemento que imprimir    
motorcycles = []
print(motorcycles[-1])
'''