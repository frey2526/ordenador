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
python ordenador.py --por-fecha          # organiza por tipo/año-mes
python ordenador.py --por-fecha --simular ~/Downloads
```

Opciones:

- Una **ruta** como argumento: la carpeta a ordenar (si no, usa `pruebas/`).
- `--simular`: modo prueba, no mueve nada.
- `--por-fecha`: además crea `tipo/AAAA-MM/` según la fecha de modificación.
- Si en el destino ya existe un archivo con el mismo nombre, **no lo pisa**:
  añade un número (`foto.jpg` → `foto (1).jpg`).

## Aprendido con este proyecto

- `pathlib` (`Path`, `parent`, `iterdir`, `suffix`, `mkdir`, `relative_to`)
- `shutil.move` para mover archivos
- Diccionarios con `set` de extensiones
- `sys.argv`: argumentos y banderas por línea de comandos
- `datetime.fromtimestamp` y `strftime("%Y-%m")` para trabajar con fechas
- `stat.st_mtime`: fecha de modificación
- `mkdir(parents=True)`: carpetas anidadas
- Idempotencia: diseñar scripts que se puedan re-ejecutar sin daño
