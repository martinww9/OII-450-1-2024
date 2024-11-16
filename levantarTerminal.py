import subprocess
import os
import sys
import platform

def abrir_terminales_ejecutar_main(n_terminals):
    current_os = platform.system() 
    if current_os not in ['Windows', 'Linux']:
        print("Sistema operativo no soportado.", file=sys.stderr)
        sys.exit(1)
    # Obtener la ruta actual del script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    programa = 'main.py'
    # Verificar que main.py existe en la ruta actual
    main_py_path = os.path.join(ruta_actual, "main.py")
    if not os.path.isfile(main_py_path):
        print(f"No se encontró {programa} en la ruta: {ruta_actual}")
        return
    # Comando para abrir una nueva ventana de terminal y ejecutar main.py
    for i in range(n_terminals):
        # Comando para abrir terminal, cambiar a la ruta actual y ejecutar main.py
        if current_os == 'Windows':
            terminal_command = f'start cmd /K "cd /d {ruta_actual} && python {programa}"'
        elif current_os == 'Linux':
            terminal_command = f'gnome-terminal -- bash -c "cd \'{ruta_actual}\' && python3 {programa}; exec bash"'
        subprocess.Popen(terminal_command, shell=True)    
    print(f"Se han abierto {n_terminals} ventanas de terminal ejecutando {programa} en la ruta: {ruta_actual}")

if __name__ == "__main__":
    print("Sistema operativo detectado:", platform.system())
    # Definir la cantidad de terminales a levantar
    n_terminals = 7 # Cambia este valor según lo que necesites
    abrir_terminales_ejecutar_main(n_terminals)