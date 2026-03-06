edad=17
if edad >18:
  print("Eres mayor de edad")
else:
 print("Eres menor de edad")
for i in range(5):
   print("hola mundo")
contador=1
while contador <=5:
  print("Numero:" + str(contador))
contador = contador + 1

for i in range(5):
    print("El Número:" + str(i))

for i in range(0,12,6):
     print("El Número:" + str(i))


encontrado =False
numerobuscado=11
numeros =[1,3,5,7,9]
for numero in numeros:
    if numero == numerobuscado:
        encontrado = True
        break
print("Número", numerobuscado, "encontrado:", encontrado)


for i in range(3):
    for j in range(3):
        print("i="+ str(i) + " j=" + str(j))