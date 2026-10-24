#this program creates a list of the first 10 cubes and then prints the list
cubes=[]

for value in range(1,11):
    cube= value**3
    cubes.append(cube)

print(cubes)