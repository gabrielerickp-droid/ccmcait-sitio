# Sitio CCMCAIT (estático)

- `paginas.py`: todo el contenido del sitio, una sección por página.
- `build.py`: genera el sitio. `python3 build.py produccion` crea `dist/` (lo que se publica en GitHub Pages).
- `src/assets/`: estilos, emblema y favicon.

Para cambiar una página: editar su bloque en `paginas.py`, ejecutar `python3 build.py produccion` y publicar `dist/`.
