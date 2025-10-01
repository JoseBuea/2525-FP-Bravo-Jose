# Tarea: Trabajo con Archivos de Texto en Python

# ==========================
# ESCRITURA DE ARCHIVO
# ==========================
# Creamos (o sobrescribimos si ya existe) un archivo llamado "my_notes.txt"
with open("my_notes.txt", "w") as file:
    # Escribimos tres notas personales
    file.write("Nota 1: Hoy practiqué programación en Python.\n")
    file.write("Nota 2: Estoy aprendiendo a manejar archivos de texto.\n")
    file.write("Nota 3: GitHub es útil para guardar mis proyectos.\n")

# ==========================
# LECTURA DE ARCHIVO
# ==========================
# Abrimos el archivo en modo lectura
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea usando readline()
    linea = file.readline()
    while linea:  # Mientras exista contenido
        print(linea.strip())  # strip() elimina saltos de línea extra
        linea = file.readline()

# ==========================
# CIERRE DE ARCHIVOS
# ==========================
# En este ejemplo, no necesitamos usar file.close() porque
# el uso de "with open()" cierra automáticamente el archivo.
