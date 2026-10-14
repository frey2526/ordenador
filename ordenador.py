from pathlib import Path
from datetime import datetime
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


def carpeta_destino(carpeta, archivo, por_fecha=False):
    """Devuelve la carpeta a la que irá 'archivo'.

    Sin fecha:  imagenes/
    Con fecha:  imagenes/2026-10/
    """
    destino = carpeta / categoria_de(archivo)
    if por_fecha:
        # st_mtime = fecha de última modificación, en segundos.
        # fromtimestamp la convierte en fecha legible; strftime la formatea.
        fecha = datetime.fromtimestamp(archivo.stat().st_mtime)
        destino = destino / fecha.strftime("%Y-%m")  # ej: "2026-10"
    return destino


def destino_libre(carpeta_destino, nombre):
    """Devuelve una ruta con nombre libre dentro de 'carpeta_destino'.

    Si 'foto.jpg' ya existe, prueba 'foto (1).jpg', 'foto (2).jpg'...
    """
    ruta = carpeta_destino / nombre
    if not ruta.exists():
        return ruta

    base = Path(nombre).stem    # "foto"
    ext = Path(nombre).suffix   # ".jpg"
    numero = 1
    while True:
        candidato = carpeta_destino / f"{base} ({numero}){ext}"
        if not candidato.exists():
            return candidato
        numero += 1


def organizar(carpeta, simular=False, por_fecha=False):
    """Mueve los archivos sueltos de 'carpeta' a subcarpetas por tipo.

    Si 'simular' es True, solo muestra lo que haría, sin tocar nada.
    Si 'por_fecha' es True, añade una subcarpeta por año-mes.
    """
    # Materializamos la lista primero: así no modificamos la carpeta mientras la leemos.
    archivos = [f for f in carpeta.iterdir() if f.is_file()]

    movidos = 0
    for archivo in archivos:
        destino = carpeta_destino(carpeta, archivo, por_fecha)
        ruta_final = destino_libre(destino, archivo.name)  # evita sobrescribir
        etiqueta = "[SIMULADO] " if simular else ""
        # Mostramos la ruta relativa: ej. imagenes/2026-10/foto.jpg
        print(f"{etiqueta}{archivo.name}  ->  {ruta_final.relative_to(carpeta)}")

        if not simular:  # solo movemos cuando NO estamos simulando
            # parents=True crea también las carpetas intermedias (imagenes/2026-10).
            destino.mkdir(parents=True, exist_ok=True)
            shutil.move(str(archivo), str(ruta_final))
        movidos += 1

    accion = "Se moverían" if simular else "Listo."
    print(f"\n{accion} {movidos} archivo(s).")


def main():
    """Decide qué carpeta ordenar y lanza el proceso."""
    # sys.argv son las palabras que escribes tras 'python ordenador.py'.
    # argv[0] es el propio script; a partir de argv[1] van tus argumentos.
    argumentos = sys.argv[1:]

    # Las banderas empiezan por "--". Las detectamos y las quitamos de la lista.
    simular = "--simular" in argumentos
    por_fecha = "--por-fecha" in argumentos
    argumentos = [a for a in argumentos if not a.startswith("--")]

    if argumentos:
        carpeta = Path(argumentos[0]).expanduser().resolve()
    else:
        carpeta = CARPETA  # sin argumentos: usamos la carpeta de pruebas

    if not carpeta.is_dir():
        print(f"Error: '{carpeta}' no es una carpeta válida.")
        return

    print(f"Ordenando: {carpeta}\n")
    organizar(carpeta, simular=simular, por_fecha=por_fecha)


if __name__ == "__main__":
    main()
