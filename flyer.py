# -*- coding: utf-8 -*-
"""Genera los flyers PDF de commodities (ES/EN) en src/assets/. Uso: python3 flyer.py"""
import base64, os
from playwright.sync_api import sync_playwright
R = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(R, "src", "assets")
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()
EMB = b64(os.path.join(A, "emblema-200.png"), "image/png")
IMG = {k: b64(os.path.join(A, "commodities", k + ".svg"), "image/svg+xml") for k in ("carbon", "minerales", "construccion", "aluminio")}
T = {
 "es": dict(lang="es", org="Cámara de Comercio Multilateral Colombo Antillana<br>de Integración y Turismo", ante="Commodities",
   h="Commodities de Colombia para el Caribe y el mundo",
   lead="Conectamos compradores, importadores y comercializadores con proveedores verificados por la Cámara.",
   prods=[("carbon","Carbón","Térmico y coquizable",""),("minerales","Minerales metálicos","Níquel, hierro y ferroaleaciones",""),
          ("construccion","Materiales de construcción","Cemento, agregados pétreos y yeso",""),("aluminio","Aluminio y no ferrosos","Chatarra, primario, billet, perfiles, chapa y bobina","Programa piloto")],
   pasos=("Cómo funciona",[("1","Nos cuenta qué necesita","Producto, volumen y destino."),("2","Verificamos y cotizamos","Solo proveedores verificados por la Cámara."),("3","Acompañamos la operación","Logística y seguimiento hasta la entrega.")]),
   nota="Especificaciones, volúmenes y precios por solicitud, según producto y destino.", cta="Solicite su cotización", web="www.ccmcait.org/commodities"),
 "en": dict(lang="en", org="Multilateral Colombian-Antillean Chamber of Commerce<br>for Integration and Tourism", ante="Commodities",
   h="Commodities from Colombia for the Caribbean and the world",
   lead="We connect buyers, importers and traders with suppliers verified by the Chamber.",
   prods=[("carbon","Coal","Thermal and coking",""),("minerales","Metallic minerals","Nickel, iron and ferroalloys",""),
          ("construccion","Construction materials","Cement, stone aggregates and gypsum",""),("aluminio","Aluminum and non-ferrous","Scrap, primary, billet, extrusions, sheet and coil","Pilot program")],
   pasos=("How it works",[("1","Tell us what you need","Product, volume and destination."),("2","We verify and quote","Only suppliers verified by the Chamber."),("3","We support the operation","Logistics and follow-up through delivery.")]),
   nota="Specifications, volumes and prices on request, depending on product and destination.", cta="Request your quote", web="www.ccmcait.org/commodities"),
}
def html(t):
    tiles = "".join(f'<div class="t"><img src="{IMG[k]}"><div class="c">' + (f'<span class="e">{e}</span>' if e else "") + f'<h3>{n}</h3><p>{d}</p></div></div>' for k, n, d, e in t["prods"])
    pasos = "".join(f'<div class="p"><b>{n}</b><div><h4>{a}</h4><p>{b}</p></div></div>' for n, a, b in t["pasos"][1])
    return f"""<!doctype html><html lang="{t['lang']}"><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}*{{box-sizing:border-box;margin:0}}
body{{width:210mm;height:297mm;font-family:'Public Sans','Segoe UI',Arial,sans-serif;color:#16202E;display:flex;flex-direction:column}}
.f{{height:6px;background:#B3242F}}
.top{{background:#0E2242;color:#fff;padding:22px 40px;display:flex;align-items:center;gap:16px}}
.top img{{width:56px;height:56px}}.top b{{font-family:Georgia,serif;font-size:22px;letter-spacing:.04em}}.top small{{display:block;font-size:10.5px;color:#C7D0DE;line-height:1.35;margin-top:2px}}
.hero{{padding:34px 40px 18px}}.ante{{font-family:'Courier New',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#A8822A}}
h1{{font-family:Georgia,serif;font-size:36px;line-height:1.12;color:#0E2242;margin:8px 0 10px}}.lead{{font-size:15px;color:#3A4658;max-width:560px}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:8px 40px 6px}}
.t{{border:1px solid #D9DEE6;background:#fff}}.t img{{width:100%;height:158px;object-fit:cover;object-position:center 58%;display:block;border-bottom:1px solid #D9DEE6}}.c{{padding:11px 14px 14px}}
.t h3{{font-family:Georgia,serif;font-size:17px;color:#0E2242;margin:4px 0 3px}}.t p{{font-size:12.5px;color:#3A4658}}
.e{{display:inline-block;font-family:'Courier New',monospace;font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;background:#F3ECDA;color:#A8822A;padding:2px 7px}}
.s{{padding:14px 40px 4px}}.s h2{{font-family:Georgia,serif;font-size:18px;color:#0E2242;margin-bottom:8px}}
.ps{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.p{{display:flex;gap:10px}}.p b{{font-family:Georgia,serif;font-size:26px;color:#A8822A;line-height:1}}
.p h4{{font-size:13px;color:#0E2242}}.p p{{font-size:11.5px;color:#3A4658;margin-top:2px}}
.n{{padding:8px 40px;font-size:11px;color:#5B6676}}
.bot{{margin-top:auto;background:#0E2242;color:#fff;padding:20px 40px;display:flex;justify-content:space-between;align-items:center}}
.bot h2{{font-family:Georgia,serif;font-size:21px}}.bot div:last-child{{text-align:right;font-size:13.5px;line-height:1.55}}.bot span{{color:#E1C47A}}
</style><body><div class="f"></div>
<div class="top"><img src="{EMB}"><div><b>CCMCAIT</b><small>{t['org']}</small></div></div>
<div class="hero"><div class="ante">{t['ante']}</div><h1>{t['h']}</h1><p class="lead">{t['lead']}</p></div>
<div class="g">{tiles}</div>
<div class="s"><h2>{t['pasos'][0]}</h2><div class="ps">{pasos}</div></div>
<div class="n">{t['nota']}</div>
<div class="bot"><div><h2>{t['cta']}</h2></div><div><span>WhatsApp</span> +57 316 468 3277<br><span>Email</span> presidencia@ccmcait.org<br><span>Web</span> {t['web']}</div></div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium") if os.path.exists("/opt/pw-browsers/chromium") and os.path.isfile("/opt/pw-browsers/chromium") else p.chromium.launch()
    for k, t in T.items():
        pg = b.new_page(); pg.set_content(html(t)); pg.wait_for_timeout(300)
        pg.pdf(path=os.path.join(A, f"flyer-commodities-{k}.pdf"), format="A4", print_background=True)
        pg.screenshot(path=f"/tmp/flyer-{k}.png", full_page=False)
    b.close()
print("ok")
