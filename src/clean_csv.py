import pandas as pd
import sys

def clean_csv(input_path, output_path):
    df = pd.read_csv(input_path)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar filas totalmente vacías
    df = df.dropna(how="all")

    # Rellenar faltantes numéricos con 0
    df = df.fillna(0)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python clean_csv.py <input.csv> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean_csv(input_file, output_file)
