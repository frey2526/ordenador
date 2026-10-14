# Ordenador de carpetas

Script en Python que ordena una carpeta llena de archivos sueltos:
los mueve a subcarpetas según su tipo (imágenes, documentos, música...).

## Qué hace

- Lee los archivos sueltos de una carpeta.
- Según su extensión, los mueve a: `imagenes/`, `documentos/`, `musica/`,
  `videos/`, `comprimidos/` o `otros/`.
- Es **idempotente**: puedes ejecutarlo varias veces sin estropear nada.

## Cómo ejecutarlo

```bash
python ordenador.py                      # ordena la carpeta de pruebas
python ordenador.py /ruta/a/mi/carpeta   # ordena la carpeta que le digas
python ordenador.py --simular            # muestra qué haría, sin tocar nada
python ordenador.py --simular ~/Downloads
```

Opciones:

- Una **ruta** como argumento: la carpeta a ordenar (si no, usa `pruebas/`).
- `--simular`: modo prueba, no mueve nada.
- Si en el destino ya existe un archivo con el mismo nombre, **no lo pisa**:
  añade un número (`foto.jpg` → `foto (1).jpg`).

## Aprendido con este proyecto

- `pathlib` (`Path`, `parent`, `iterdir`, `suffix`, `mkdir`)
- `shutil.move` para mover archivos
- Diccionarios con `set` de extensiones
- Argumentos y banderas por línea de comandos (`sys.argv`)
- Idempotencia: diseñar scripts que se puedan re-ejecutar sin daño
