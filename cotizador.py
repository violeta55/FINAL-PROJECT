print("Bienvenido al cotizador de viajes ExploraMundo")
destinos = {"Cartagena": 250000, "Medellín": 200000, "San Andrés": 300000}
destino = input("Elige un destino (Cartagena, Medellín, San Andrés): ")
personas = int(input("Número de personas: "))
dias = int(input("Cantidad de días: "))

if destino in destinos:
    total = destinos[destino] * personas * dias
    print(f"Costo total para {personas} personas por {dias} días en {destino}: ${total}")
else:
    print("Destino no disponible.")
    