from pathlib import Path

# Carpeta donde están las imágenes
carpeta = Path(r"C:\Users\Sinai.Cabrera\Documents\VSC\camera_detector\dataset")

# Número inicial
inicio = 400

# Obtener todos los archivos y ordenarlos por nombre
archivos = sorted([f for f in carpeta.iterdir() if f.is_file()])

for i, archivo in enumerate(archivos, start=inicio):
    nuevo_nombre = f"img_0{i:03d}{archivo.suffix}"
    nuevo_path = carpeta / nuevo_nombre

    archivo.rename(nuevo_path)
    print(f"{archivo.name} -> {nuevo_nombre}")

print("Renombrado completado.")