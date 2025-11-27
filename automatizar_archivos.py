import os
from datetime import datetime

# Carpeta donde están tus archivos
carpeta = "C:/TODO/PROGRAMAS/LABORAL/freelancer base/archivos"

# Iterar sobre los archivos
for nombre_archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    if os.path.isfile(ruta_completa):
        # Obtener fecha de creación
        timestamp = os.path.getctime(ruta_completa)
        fecha = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        # Nuevo nombre: fecha_original
        nuevo_nombre = f"{fecha}_{nombre_archivo}"
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)

        # Renombrar
        os.rename(ruta_completa, nueva_ruta)
        print(f"Renombrado: {nombre_archivo} → {nuevo_nombre}")
