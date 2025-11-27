import pandas as pd
import sys

def generate_report(input_path, output_path):
    df = pd.read_csv(input_path)

    report = {}

    # Filas y columnas
    report["shape"] = df.shape

    # Nombres de columnas
    report["columns"] = list(df.columns)

    # Conteo de valores faltantes por columna
    report["missing"] = df.isna().sum().to_dict()

    # Descripción estadística para columnas numéricas
    report["describe"] = df.describe(include="all").to_dict()

    # Guardar reporte en texto simple
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in report.items():
            f.write(f"{key}:\n{value}\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python report_csv.py <input.csv> <output.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    generate_report(input_file, output_file)
