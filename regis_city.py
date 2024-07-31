import carga_guarda as gg

def registro():
    data = gg.cargar_city()
    while True:
        try:
            cd_postal = int(input("Digite el codigo postal de la ciudad que vas añadir: "))
            break
        except Exception:
            print("Digite bien los datos")
    if str(cd_postal) in data["Ciudades"]:
        print("Ya hay una ciudad registrada con este codigo postal!!")
        print("*****************************************************")
    else:
        datos = {}
        datos["Nombre ciudad"] = str(input("Digite el nombre de  la ciudad :"))
        datos["Codigo Postal"] = cd_postal
        while True:
            try:
                datos["Poblacion"] = int(input("Digite la poblacion de  la ciudad :"))
                break
            except Exception:
                print("Digite bien los datos")
        datos["Pais"] = str(input("Digite el pais de  la ciudad :"))
        data["Ciudades"][cd_postal] = datos
        gg.guardar_city(data)
        
registro()