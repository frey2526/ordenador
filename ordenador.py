from pathlib import Path
import shutil
import sys

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


def organizar(carpeta, simular=False):
    """Mueve los archivos sueltos de 'carpeta' a subcarpetas por tipo.

    Si 'simular' es True, solo muestra lo que haría, sin tocar nada.
    """
    # Materializamos la lista primero: así no modificamos la carpeta mientras la leemos.
    archivos = [f for f in carpeta.iterdir() if f.is_file()]

    movidos = 0
    for archivo in archivos:
        destino = carpeta / categoria_de(archivo)   # ej: pruebas / imagenes
        etiqueta = "[SIMULADO] " if simular else ""
        print(f"{etiqueta}{archivo.name}  ->  {destino.name}/")

        if not simular:  # solo movemos cuando NO estamos simulando
            destino.mkdir(exist_ok=True)  # crea la subcarpeta si no existe
            shutil.move(str(archivo), str(destino / archivo.name))
        movidos += 1

    accion = "Se moverían" if simular else "Listo."
    print(f"\n{accion} {movidos} archivo(s).")


def main():
    """Decide qué carpeta ordenar y lanza el proceso."""
    # sys.argv son las palabras que escribes tras 'python ordenador.py'.
    # argv[0] es el propio script; a partir de argv[1] van tus argumentos.
    argumentos = sys.argv[1:]

    # Buscamos la bandera --simular y la quitamos de la lista.
    simular = "--simular" in argumentos
    argumentos = [a for a in argumentos if a != "--simular"]

    if argumentos:
        carpeta = Path(argumentos[0]).expanduser().resolve()
    else:
        carpeta = CARPETA  # sin argumentos: usamos la carpeta de pruebas

    if not carpeta.is_dir():
        print(f"Error: '{carpeta}' no es una carpeta válida.")
        return

    print(f"Ordenando: {carpeta}\n")
    organizar(carpeta, simular=simular)


if __name__ == "__main__":
    main()
