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