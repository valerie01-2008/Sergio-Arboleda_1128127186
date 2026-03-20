estudiantes= ["Juan", " lianna", "laura", "marcos", "shayla", "valerie", "maria", "adriana", "xavi", "keiner"]
 
 #agragar un nuevo estudiante al final
estudiantes.append("edwin")
print(estudiantes) # ['Juan', ' lianna', 'laura', 'marcos', 'shayla', 'valerie', 'maria', 'adriana', 'xavi', 'keiner', 'edwin'

#obtener el numero de estudiantes
print(len(estudiantes)) #11

#buscar si un estudiante esta en la lista
if "marcos" in estudiantes:
    print("marcos esta en la lista de estudiantes")

#eliminar un estudiante de la lista
estudiantes.remove("shayla")
print(estudiantes) # ['Juan', ' lianna', 'laura', 'marcos', 'valerie', 'maria', 'adriana', 'xavi', 'keiner', 'edwin']


