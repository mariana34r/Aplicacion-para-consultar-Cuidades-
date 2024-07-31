import letreros
import regis_city
import edit_city
import mostrar_city
import mostrar_todas


print("jajajajja")
print("hola mundo")
print("Binevenido :)")
print("Ingrese su Nombre Usuario")
Nombre=input("-")
print("Binevenido",Nombre)
while True:
    print("Que desea hacer ")
    print("--------------------------")
    print("1 Crear cuidades\n2.Editar Cuidades\n3.Mostrar Cuidades\n4.Buscar Cuidades\n5.Salir")
    print("--------------------------")
    print("Escoga una Opcion")
    try:
        opc = input("-")
        if opc == '1':
            letreros.letrero1()
            regis_city.registro()
        elif opc == '2':
            letreros.letrero2()
            edit_city.editar_city()
        elif opc == '3':
            letreros.letrero3()
            mostrar_todas.todo()
            
        elif opc == '4':
            letreros.letrero4()
            mostrar_city.mostra_ciudad()
            
        elif opc == '5':
            letreros.letrero5()
            break  
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
    
    except Exception :
        print("Ingrese una opcion valida")
        
        
        