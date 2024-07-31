import carga_guarda as gg
def todo():
    while True:
        data = gg.cargar_city()
        print("1. Para ver todas las ciudades")
        print("2. Para salir")
        while True:
            try:
                opc = int(input("DIgite una opcion: "))
                break
            except Exception:
                print("opcion no valida")
        if opc == 1:
            for m, n in data.items():
                for s, j in n.items():
                    print("****************************************************************")
                    print("La ciudad con el codigo postal", s, "\ncon el nombre", data["Ciudades"][str(s)]["Nombre ciudad"],"\ncon la poblacion", data["Ciudades"][str(s)]["Poblacion"],"\nque se encuentra en el pais", data["Ciudades"][str(s)]["Pais"])
        elif opc ==2:
            print("saliendo...")
            break
        else:
            print("opcion invalida")                    


