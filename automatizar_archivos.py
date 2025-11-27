import os
import time

import pandas as pd

carpeta = "archivos"
os.makedirs(carpeta, exist_ok=True)

# 1. Crear CSV de ejemplo
for i in range(3):
    df = pd.DataFrame({
        "A": [1,2,3],
        "B": [4,5,6]
    })
    df.to_csv(os.path.join(carpeta, f"ejemplo{i}.csv"), index=False)

# 2. Crear archivos de texto
for i in range(2):
    with open(os.path.join(carpeta, f"doc{i}.txt"), "w") as f:
        f.write("Este es un archivo de prueba\n" * 5)

# 3. Crear archivos de imagen vacíos (simples .jpg)
for i in range(2):
    with open(os.path.join(carpeta, f"imagen{i}.jpg"), "wb") as f:
        f.write(b"\x00\x00\x00\x00")  # archivo vacío, suficiente para mover/renombrar

print("revisá")
time.sleep(5)

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


import os
import shutil

carpeta = "archivos"  # carpeta origen
destinos = {
    "imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "csv": [".csv"]
}

for archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta):
        _, ext = os.path.splitext(archivo)
        for carpeta_dest, extensiones in destinos.items():
            if ext.lower() in extensiones:
                destino = os.path.join(carpeta, carpeta_dest)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta, os.path.join(destino, archivo))
                print(f"Movido: {archivo} → {carpeta_dest}")
import pandas as pd
import os

carpeta = "archivos/csv"
for archivo in os.listdir(carpeta):
    if archivo.endswith(".csv"):
        ruta_csv = os.path.join(carpeta, archivo)
        df = pd.read_csv(ruta_csv)
        ruta_excel = os.path.join(carpeta, archivo.replace(".csv", ".xlsx"))
        df.to_excel(ruta_excel, index=False)
        print(f"Convertido: {archivo} → {archivo.replace('.csv', '.xlsx')}")

import os
import shutil
from datetime import datetime
import pandas as pd

carpeta = "archivos"

# 1. Renombrar archivos agregando fecha de creación
for nombre_archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, nombre_archivo)
    if os.path.isfile(ruta):
        fecha = datetime.fromtimestamp(os.path.getctime(ruta)).strftime("%Y-%m-%d")
        nuevo_nombre = f"{fecha}_{nombre_archivo}"
        os.rename(ruta, os.path.join(carpeta, nuevo_nombre))

# 2. Mover archivos por tipo
destinos = {
    "imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "csv": [".csv"]
}

for archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta):
        _, ext = os.path.splitext(archivo)
        for carpeta_dest, extensiones in destinos.items():
            if ext.lower() in extensiones:
                destino = os.path.join(carpeta, carpeta_dest)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta, os.path.join(destino, archivo))

# 3. Convertir CSV a Excel
csv_carpeta = os.path.join(carpeta, "csv")
if os.path.exists(csv_carpeta):
    for archivo in os.listdir(csv_carpeta):
        if archivo.endswith(".csv"):
            ruta_csv = os.path.join(csv_carpeta, archivo)
            df = pd.read_csv(ruta_csv)
            ruta_excel = os.path.join(csv_carpeta, archivo.replace(".csv", ".xlsx"))
            df.to_excel(ruta_excel, index=False)

# 4. Resumen de archivos
print("Resumen de archivos:")
for root, dirs, files in os.walk(carpeta):
    for archivo in files:
        ruta = os.path.join(root, archivo)
        tamaño = os.path.getsize(ruta)
        print(f"{ruta} → {tamaño} bytes")









