import file_manager
import statistics

def calculate_statistics():
    stored_files = file_manager.get_stored_files()
    if not stored_files:
        print("No hay información almacenada para calcular estadísticas.")
        return

    stat_names = []
    stat_values = []

    for file_name in stored_files:
        data = file_manager.load_pokemon_info(file_name)
        stats = data["stats"]
        for stat, value in stats.items():
            stat_names.append(stat)
            stat_values.append(value)

    total_files = len(stored_files)
    print(f"Estadísticas basadas en {total_files} archivo{'s' if total_files > 1 else ''}:")
    print("------------------")

    unique_stats = set(stat_names)

    for stat in unique_stats:
        values = [value for name, value in zip(stat_names, stat_values) if name == stat]

        average = statistics.mean(values)
        minimum = min(values)
        maximum = max(values)
        mode = statistics.mode(values)

        print(f"Estadística: {stat}")
        print(f"Promedio: {average:.2f}")
        print(f"Mínimo: {minimum}")
        print(f"Máximo: {maximum}")
        print(f"Moda: {mode}")
        print("------------------")
