#!/usr/bin/env python3
"""Genera el sitio estático de CCMCAIT.

Uso:
  python3 build.py produccion   -> carpeta dist/ (lista para GitHub Pages, URLs limpias)
  python3 build.py vista        -> carpeta vista/ (vista previa, enlaces a index.html)

Para actualizar una página: editar su bloque en paginas.py y volver a ejecutar.
"""
import os, re, shutil, sys, datetime
from paginas import PAGINAS, REDIRECCIONES, NAV, SITIO

MODO = sys.argv[1] if len(sys.argv) > 1 else "produccion"
SALIDA = "dist" if MODO == "produccion" else "vista"
RAIZ = os.path.dirname(os.path.abspath(__file__))


def url(destino, profundidad):
    """Enlace relativo a una página interna ('' es inicio)."""
    prefijo = "../" * profundidad
    if MODO == "produccion":
        return prefijo + (destino + "/" if destino else "") or "./"
    return prefijo + (destino + "/" if destino else "") + "index.html"


def resolver(html, profundidad):
    html = re.sub(r"\{\{u:([a-z0-9\-]*)\}\}", lambda m: url(m.group(1), profundidad), html)
    html = html.replace("{{a}}", "../" * profundidad + "assets/")
    return html


def cabecera(slug, profundidad):
    enlaces = []
    for destino, nombre in NAV:
        actual = ' aria-current="page"' if destino == slug or (destino and slug in PAGINAS.get(destino, {}).get("hijas", [])) else ""
        enlaces.append(f'<a href="{{{{u:{destino}}}}}"{actual}>{nombre}</a>')
    nav = "".join(enlaces)
    return f"""<div class="franja"></div>
<header class="cabecera"><div class="envoltura">
<a class="marca" href="{{{{u:}}}}"><img src="{{{{a}}}}emblema-200.png" alt="Emblema de la CCMCAIT" width="48" height="48"><span><b>CCMCAIT</b><small>Cámara de Comercio Multilateral Colombo Antillana<br>de Integración y Turismo</small></span></a>
<nav class="nav" aria-label="Principal">{nav}</nav>
<details class="menu-movil"><summary>Menú</summary><nav aria-label="Principal móvil">{nav}</nav></details>
</div></header>"""


def pie():
    return f"""<footer class="pie"><div class="envoltura">
<div class="rejilla-pie">
<div><h4>CCMCAIT</h4><p>Cámara de Comercio Multilateral Colombo Antillana de Integración y Turismo. Entidad sin ánimo de lucro. Puente institucional entre Colombia y 34 países y territorios del Caribe y las Antillas.</p></div>
<div><h4>La Cámara</h4><a href="{{{{u:sobre-la-camara}}}}">Sobre la Cámara</a><a href="{{{{u:como-lo-hacemos}}}}">Cómo lo hacemos</a><a href="{{{{u:tratados}}}}">Tratados</a><a href="{{{{u:aliados-estrategicos}}}}">Aliados estratégicos</a></div>
<div><h4>Negocios</h4><a href="{{{{u:servicios}}}}">Servicios</a><a href="{{{{u:cobertura}}}}">Cobertura</a><a href="{{{{u:portal-de-oportunidades}}}}">Portal de oportunidades</a><a href="{{{{u:casos-de-exito}}}}">Casos de éxito</a><a href="{{{{u:eventos}}}}">Eventos</a></div>
<div><h4>Contacto</h4><a href="{{{{u:contacto}}}}">Escríbenos</a><a href="https://wa.me/{SITIO['whatsapp']}">WhatsApp +57 316 468 3277</a><a href="https://www.instagram.com/camaracolomboantillana/">Instagram</a><a href="https://x.com/ccmcait">X</a></div>
</div>
<div class="legal"><span>© {datetime.date.today().year} CCMCAIT · Bogotá · Santo Domingo</span><a href="{{{{u:privacidad}}}}">Aviso de privacidad y tratamiento de datos</a></div>
</div></footer>
<a class="whatsapp" href="https://wa.me/{SITIO['whatsapp']}" aria-label="Escríbenos por WhatsApp">WhatsApp</a>"""


def documento(slug, pag, profundidad):
    canonical = SITIO["dominio"] + (slug + "/" if slug else "")
    script = ""
    if MODO == "vista":
        script = """<script>document.querySelectorAll('form[data-formulario]').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var n=f.querySelector('[data-nota]');if(n){n.hidden=false;}});});</script>"""
    cuerpo = cabecera(slug, profundidad) + "<main>" + pag["html"] + "</main>" + pie() + script
    return resolver(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{pag['titulo']}</title>
<meta name="description" content="{pag['descripcion']}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{pag['titulo']}">
<meta property="og:description" content="{pag['descripcion']}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<link rel="icon" type="image/png" href="{{{{a}}}}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Public+Sans:wght@400;600&family=Spectral:wght@500;600&display=swap">
<link rel="stylesheet" href="{{{{a}}}}estilo.css">
</head>
<body>
{cuerpo}
</body>
</html>
""", profundidad)


def redireccion(destino, profundidad):
    href = resolver(f"{{{{u:{destino}}}}}", profundidad)
    canon = SITIO["dominio"] + (destino + "/" if destino else "")
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Redirigiendo…</title>
<link rel="canonical" href="{canon}"><meta http-equiv="refresh" content="0; url={href}"><meta name="robots" content="noindex"></head>
<body><p>Esta página cambió de lugar. <a href="{href}">Continuar</a>.</p></body></html>"""


def main():
    out = os.path.join(RAIZ, SALIDA)
    shutil.rmtree(out, ignore_errors=True)
    shutil.copytree(os.path.join(RAIZ, "src", "assets"), os.path.join(out, "assets"))
    for slug, pag in PAGINAS.items():
        prof = 1 if slug else 0
        carpeta = os.path.join(out, slug) if slug else out
        os.makedirs(carpeta, exist_ok=True)
        with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(documento(slug, pag, prof))
    for viejo, nuevo in REDIRECCIONES.items():
        os.makedirs(os.path.join(out, viejo), exist_ok=True)
        with open(os.path.join(out, viejo, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(redireccion(nuevo, 1))
    if MODO == "produccion":
        # 404 con rutas absolutas (se sirve en cualquier profundidad)
        pag = {"titulo": "Página no encontrada | CCMCAIT", "descripcion": "La página que buscas no existe.",
               "html": '<section class="heroe interior"><div class="envoltura"><div class="copia"><p class="ante">Error 404</p><h1>Esta página no existe</h1><p class="lead">Es posible que el enlace haya cambiado con la renovación del sitio.</p><div class="acciones"><a class="boton" href="/">Ir al inicio</a><a class="boton sec" href="/contacto/">Contactar a la Cámara</a></div></div></div></section>'}
        html = documento("404", pag, 0)
        html = re.sub(r'href="(?!https?:|/|#)([^"]*)"', lambda m: 'href="/' + m.group(1).lstrip("./") + '"', html)
        html = re.sub(r'src="(?!https?:|/)([^"]*)"', lambda m: 'src="/' + m.group(1).lstrip("./") + '"', html)
        open(os.path.join(out, "404.html"), "w", encoding="utf-8").write(html)
        open(os.path.join(out, "CNAME"), "w").write("www.ccmcait.org\n")
        open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITIO['dominio']}sitemap.xml\n")
        hoy = datetime.date.today().isoformat()
        urls = "".join(f"<url><loc>{SITIO['dominio']}{(s + '/') if s else ''}</loc><lastmod>{hoy}</lastmod></url>" for s, p in PAGINAS.items() if not p.get("noindex"))
        open(os.path.join(out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
        open(os.path.join(out, ".nojekyll"), "w").write("")
    print(f"Sitio generado en {SALIDA}/ ({len(PAGINAS)} páginas, {len(REDIRECCIONES)} redirecciones)")


if __name__ == "__main__":
    main()
