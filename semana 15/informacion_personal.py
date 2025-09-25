# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Jose Bravo",
    "edad": 18,
    "ciudad": "Pasaje",
    "profesion": "Tecnologia"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "El oro"

# Agregar una nueva clave-valor "profesion" (cambiándola o complementándola)
informacion_personal["profesion"] = "Tecnologia"

# Verificar si "telefono" existe; si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir el diccionario final
for key, value in informacion_personal.items():
    print(f"{key}: {value}")