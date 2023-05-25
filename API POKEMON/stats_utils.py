import file_manager

def calculate_statistics():
    stored_files = file_manager.get_stored_files()
    if not stored_files:
        print("No hay información almacenada para calcular estadísticas.")
        return

    stat_values = []
    stats_count = {}

    for file_name in stored_files:
        data = file_manager.load_pokemon_info(file_name)
        stats = data["stats"]
        for stat, value in stats.items():
            stat_values.append(value)
            if stat not in stats_count:
                stats_count[stat] = []
            stats_count[stat].append(value)

    total_files = len(stored_files)
    print(f"Estadísticas basadas en {total_files} archivo{'s' if total_files > 1 else ''}:")
    print("------------------")

    for stat, values in stats_count.items():
        average = sum(values) / len(values)
        minimum = min(values)
        maximum = max(values)
        mode = get_mode(values)

        print(f"Estadística: {stat}")
        print(f"Promedio: {average:.2f}")
        print(f"Mínimo: {minimum}")
        print(f"Máximo: {maximum}")
        print(f"Moda: {mode}")
        print("------------------")

def get_mode(values):
    count_dict = {}
    for value in values:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    
    max_count = max(count_dict.values())
    modes = [value for value, count in count_dict.items() if count == max_count]
    
    if len(modes) == len(values):
        return "No hay moda"
    else:
        return ", ".join(str(mode) for mode in modes)
