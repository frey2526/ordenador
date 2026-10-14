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
python ordenador.py
```

Por defecto trabaja sobre la carpeta `pruebas/`, creada para hacer test sin
tocar archivos reales.

## Aprendido con este proyecto

- `pathlib` (`Path`, `parent`, `iterdir`, `suffix`, `mkdir`)
- `shutil.move` para mover archivos
- Diccionarios con `set` de extensiones
- Idempotencia: diseñar scripts que se puedan re-ejecutar sin daño
