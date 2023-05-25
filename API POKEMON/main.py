import api
import file_manager
import stats_utils
import graph_generator

def main():
    while True:
        print("-------- Pokedex --------")
        print("1. Consultar información de un Pokemon")
        print("2. Consultar información almacenada")
        print("3. Mostrar estadísticas")
        print("4. Generar gráficas")
        print("5. Salir")

        choice = input("Ingrese su opción: ")
        if choice == "1":
            pokemon_name = input("Ingrese el nombre de un Pokemon: ")
            data = api.get_pokemon_info(pokemon_name)
            if data:
                print("\nInformación del Pokemon:")
                print(f"Nombre: {data['name']}")
                print(f"Altura: {data['height']} dm")
                print(f"Peso: {data['weight']} hg")
                print(f"Habilidades: {', '.join(data['abilities'])}")
                print(f"Estadísticas: {', '.join(f'{stat}: {value}' for stat, value in data['stats'].items())}")
                save_choice = input("¿Desea guardar esta información? (S/N): ")
                if save_choice.upper() == "S":
                    file_manager.save_pokemon_info(data)
                    print("La información se ha guardado correctamente.")
            else:
                print("No se encontró información para ese Pokemon.")
        elif choice == "2":
            stored_files = file_manager.get_stored_files()
            if not stored_files:
                print("No hay información almacenada.")
                continue
            print("Archivos almacenados:")
            for i, file_name in enumerate(stored_files):
                print(f"{i + 1}. {file_name}")
            file_choice = input("Ingrese el número del archivo que desea consultar: ")
            if file_choice.isdigit() and int(file_choice) in range(1, len(stored_files) + 1):
                file_name = stored_files[int(file_choice) - 1]
                data = file_manager.load_pokemon_info(file_name)
                print("\nInformación del Pokemon:")
                print(f"Nombre: {data['name']}")
                print(f"Altura: {data['height']} dm")
                print(f"Peso: {data['weight']} hg")
                print(f"Habilidades: {', '.join(data['abilities'])}")
                print(f"Estadísticas: {', '.join(f'{stat}: {value}' for stat, value in data['stats'].items())}")
            else:
                print("Opción inválida.")
        elif choice == "3":
            stats_utils.calculate_statistics()
        elif choice == "4":
            graph_generator.generate_graphs()
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()
