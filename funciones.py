#2do intentoPrueba 3 inicio: 10:00am - 14:00pm(receso), Continua: 15:00pm - 17:00 Termino

import json #Para acceder a la informacion
# r = Leer w = Escribir
#Agregar cliente 3 variables

def agregar_usuario(Nombre:str, Email:str, FechaRegistro:str): #Definir mi funcion y variables 
    with open("biblioteca.json", mode="r") as agregar_json:    #With open accede y cierra el json de biblioteca y el as se encarga de ayudarme a no poner constantemente "biblioteca json"
        r = json.load(agregar_json)                            #r es mi variable que leera el json  
        usuarios ={
            "UsuarioID": len(r["Usuario"])+1,                                #len usa tu variable que lee el json para luego acceder a la seccion del json que deseas modificar (en este caso "Usuarios") el +1 es para que el ID no se repita
            "Nombre": Nombre, 
            "Email": Email,
            "FechaRegistro": FechaRegistro
            }
        r["Usuario"].append(usuarios)                          #r accede a usuarios y junto a append agregar al final del json los elementos agregados
    
    with open("biblioteca.json", mode="w") as agregar_json:    #Cambia el modo de lectura= r a Escribir = w
        json.dump(r,agregar_json,indent= 4)                    #Json.dump es para agregar informacion en un lugar en especifico y el indent es para los espacios y tabulaciones
    print("El Nuevo usuario a sido agregado exitosamente.")    #Se imprimira este mensaje al agregar al nuevo usuario


#Editarcliente 4 variables

def editar_usuario(UsuarioID:int, Nombre:str, Email:str, FechaRegistro:str):
    with open("biblioteca.json",mode="r") as editar_json:
        r= json.load(editar_json)
        BuscadorID = False                                      # Se usa False porque aun no se a encontrado al usuario
        for repeticion in r["Usuario"]:
            if repeticion["UsuarioID"]== UsuarioID:                         #repeticion recorrera todos los USUARIOS ID del json
                repeticion["Nombre"]= Nombre
                repeticion["Email"]= Email
                repeticion["FechaRegistro"]= FechaRegistro
                BuscadorID = True
                break
        if not BuscadorID:                                                  #if not = sino
            print("El usuario ingresado no se ha encontrado!!.")         
        else:
            with open("biblioteca.json", mode="w") as editar_json:
                json.dump(r,editar_json,indent= 4)
            print("El usuario se a modificado correctamente.")
                
#Eliminar cliente 1 variable

def eliminar_usuario(IDeliminar):
    with open("biblioteca.json", mode="r") as delete_ID:
        r= json.load(delete_ID)
        BuscadorID2 = False
        for j,user in enumerate(r["Usuario"]):              #enumerate = se encarga de mandarle la orden al for de que recorra todas las variables ( en este caso j, user) 
            if user["UsuarioID"] == IDeliminar:
                r["Usuario"].pop(j)                              #.pop es para eliminar
                BuscadorID2= True
                break
        if not BuscadorID2:
            print("el usuario que esta buscando no se encuentra en el sistema.")
        else:
            for k in range(j,len(r["Usuario"])):
                r["Usuario"][k]["UsuarioID"]-=1                 #-=1 Se encarga de ir asignando los numeros de lista de manera correcta a los usuarios en el json
            with open("biblioteca.json", mode="w") as delete_ID:
                json.dump(r,delete_ID,indent= 4)
            print("Se ha borrado de manera correcta al usuario seleccionado.")

        
#Listar clientes 1 variable

def lista_usuarios(Lista_users):
    with open("biblioteca.json", mode= "r") as listar_json:
        r=json.load(listar_json)
        print(r["Usuario"])
        
    







