import file_manager
import matplotlib.pyplot as plt

def generate_graphs():
    stored_files = file_manager.get_stored_files()
    if not stored_files:
        print("No hay información almacenada para generar gráficas.")
        return
    print("Archivos almacenados:")
    for i, file_name in enumerate(stored_files):
        print(f"{i + 1}. {file_name}")
    file_choice = input("Ingrese el número del archivo que desea visualizar: ")
    if file_choice.isdigit() and int(file_choice) in range(1, len(stored_files) + 1):
        file_name = stored_files[int(file_choice) - 1]
        data = file_manager.load_pokemon_info(file_name)
        stats = data["stats"]
        stat_names = list(stats.keys())
        stat_values = list(stats.values())
        plt.figure(figsize=(8, 6))
        plt.bar(stat_names, stat_values)
        plt.xlabel("Estadística")
        plt.ylabel("Valor")
        plt.title("Estadísticas del Pokemon")
        plt.grid(True)
        plt.show()
    else:
        print("Opción inválida.")
