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
    print("------------------------------")
    print("Promedio por estadística:")
    for stat in set(stat_names):
        values = [value for name, value in zip(stat_names, stat_values) if name == stat]
        average = statistics.mean(values)
        print(f"{stat}: {average:.2f}")
    print("------------------------------")
    print("Mínimo por estadística:")
    for stat in set(stat_names):
        values = [value for name, value in zip(stat_names, stat_values) if name == stat]
        minimum = min(values)
        print(f"{stat}: {minimum}")
    print("------------------------------")
    print("Máximo por estadística:")
    for stat in set(stat_names):
        values = [value for name, value in zip(stat_names, stat_values) if name == stat]
        maximum = max(values)
        print(f"{stat}: {maximum}")
    print("------------------------------")
    print("Moda por estadística:")
    for stat in set(stat_names):
        values = [value for name, value in zip(stat_names, stat_values) if name == stat]
        mode = statistics.mode(values)
        print(f"{stat}: {mode}")
