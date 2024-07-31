import carga_guarda as gg
def menu():
    menu = ["1. Para Nombre de la ciudad", "2. Para la poblacion de la ciudad", "3. Para el pais", "4. Salir"]
    for n in menu:
        print(n)


def editar_city():
    while True:
        data = gg.cargar_city()
        while True:
            try:
                cd_postal = int(input("Digite el codigo postal de la ciudad que vas a editar presiona 0 si quieres salir: "))
                break
            except Exception:
                print("Digite bien los datos")
    
        if str(cd_postal) in data["Ciudades"]:
            while True:
                menu()
                while True:
                    try:
                        op = int(input("Seleccione una opcion: "))
                        break
                    except Exception:
                        print("opcion no validaa")
                if op == 1:
                    nuevo = str(input("Digite el nuevo nombre de la ciudad: "))
                    data["Ciudades"][str(cd_postal)]["Nombre ciudad"] = nuevo
                    gg.guardar_city(data)
                    
                elif op == 2:
                    nuevo = int(input("Digite la nuevo poblacion de la ciudad: "))
                    data["Ciudades"][str(cd_postal)]["Poblacion"] = nuevo
                    gg.guardar_city(data)
                    
                elif op == 3:
                    nuevo = (input("Digite pais de la ciudad: "))
                    data["Ciudades"][str(cd_postal)]["Pais"] = nuevo
                    gg.guardar_city(data)
                    
                elif op == 4:
                    print("Saliendo...")
                    break
                else:
                    print("opcion invalida")
            break
        elif cd_postal == 0:
            print("Saliendo...")
            break
        
