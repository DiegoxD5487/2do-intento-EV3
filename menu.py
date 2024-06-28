#2do intentoPrueba 3 inicio: 10:00am - 14:00pm(receso), Continua: 15:00pm - 17:00 Termino

from funciones import *    # * para traer todo 

print("************************")
print("*     MUNDO LIBRO      *")      #Mensaje de biblioteca
print("************************")

#Profesor no se como hacer el menu dentro de otro menu :(

menu1 = ("Agregar Usuario","Editar Usuario","Eliminar Usuario", "Listar Usuarios", "Salir") #Opciones menu (Tupla)
contador = 0                                                    #Contador porque habra un blucle for

for i in menu1:
    contador +=1                                                          
    print(f"[{contador}].-{i}")                                 #Entiendo que su funcion es mostrar la tupla en orden y que el ".-" es para la presentacion

while True:                                                     #While True es para que el programa no finalice hasta escoger "Salir"
    opcion = int(input("Escoger opcion disponible :"))
    if  opcion == 1:                                            #Uso "=="porque voy a comparar valores en cambio "=" Es solo par adar valor a una variable
        Nombre = str(input("Ingresar el nombre del nuevo usuario :"))
        Email = str(input("Ingresar Emai del nuevo usuario :"))
        FechaRegistro = str(input("Ingresar fecha del día :"))
        agregar_usuario(Nombre, Email, FechaRegistro)          #Llamo a la funcion"""

    elif opcion == 2:
        usuarioID = int(input("Ingresar el ID del cliente que desea modificar :"))
        Nombre = str(input("Ingresar nuevo nomnbre :"))
        Email = str (input("Ingresar nuevo Email :"))
        FechaRegistro = str (input("Fecha de actualizacion de información :"))
        editar_usuario(usuarioID, Nombre, Email, FechaRegistro)

    elif opcion == 3:
        IDeliminar = int(input("Ingresar el ID del usuario que desea eliminar permanentemente :"))
        eliminar_usuario(IDeliminar)

    elif opcion == 4:
        Lista_Users =str
        lista_usuarios(Lista_Users)

    elif opcion == 5:

        print("Has salido del menú de opciones.")
        break
    
    #Para que el ciclo no se repita infinitamente


    