from pathlib import Path
import shutil

# La carpeta que vamos a ordenar. De momento es "pruebas".
CARPETA = Path(__file__).parent / "pruebas"

# Mapa: nombre de la subcarpeta -> extensiones que van ahí.
CATEGORIAS = {
    "imagenes": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documentos": {".pdf", ".txt", ".docx", ".odt"},
    "musica": {".mp3", ".wav", ".flac"},
    "videos": {".mp4", ".mkv", ".mov"},
    "comprimidos": {".zip", ".rar", ".7z"},
}


def categoria_de(archivo):
    """Devuelve la subcarpeta a la que pertenece un archivo según su extensión."""
    for nombre, extensiones in CATEGORIAS.items():
        if archivo.suffix.lower() in extensiones:
            return nombre
    return "otros"  # cualquier extensión desconocida cae aquí


def organizar(carpeta):
    """Mueve los archivos sueltos de 'carpeta' a subcarpetas por tipo."""
    # Materializamos la lista primero: así no modificamos la carpeta mientras la leemos.
    archivos = [f for f in carpeta.iterdir() if f.is_file()]

    movidos = 0
    for archivo in archivos:
        destino = carpeta / categoria_de(archivo)   # ej: pruebas / imagenes
        destino.mkdir(exist_ok=True)                # crea la subcarpeta si no existe
        shutil.move(str(archivo), str(destino / archivo.name))
        print(f"{archivo.name}  ->  {destino.name}/")
        movidos += 1

    print(f"\nListo. {movidos} archivo(s) organizado(s).")


if __name__ == "__main__":
    organizar(CARPETA)
