import carga_guarda as gg

def mostra_ciudad():
    data = gg.cargar_city()
    while True:
        try:
            cd_postal = int(input("Digite el codigo postal de la ciudad que vas a mostrar: "))
            break
        except Exception:
            print("Digite bien los datos")
    if str(cd_postal) in data["Ciudades"]:
        print("La ciudad", data["Ciudades"][str(cd_postal)]["Nombre ciudad"], "Con la poblacion", data["Ciudades"][str(cd_postal)]["Poblacion"], "que se encuentra en el pais", data["Ciudades"][str(cd_postal)]["Pais"])

