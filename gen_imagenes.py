# -*- coding: utf-8 -*-
"""Ilustraciones de producto (carbón, minerales, construcción, aluminio) con luz y facetas. Uso: python3 gen_imagenes.py"""
import random, math, os
W, H = 640, 440
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "assets", "commodities")
def hexrgb(h): h = h.lstrip("#"); return [int(h[i:i+2], 16) for i in (0, 2, 4)]
def mix(c, t):  # t<0 oscurece, t>0 aclara
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(v + (255 - v) * t if t > 0 else v * (1 + t)))) for v in c)
def chunk(cx, cy, r, base, rnd, n=9, flat=.72, spec=None):
    base = hexrgb(base); ang = sorted(rnd.uniform(0, 2 * math.pi) for _ in range(n))
    pts = [(cx + math.cos(a) * r * rnd.uniform(.72, 1.05), cy + math.sin(a) * r * flat * rnd.uniform(.72, 1.05) - r * .1) for a in ang]
    top = (cx - r * .15, cy - r * .55)
    s = ""
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        mx, my = (p[0] + q[0]) / 2 - cx, (p[1] + q[1]) / 2 - cy
        d = math.hypot(mx, my) or 1; lum = (-mx / d * .6 - my / d * .8)  # luz arriba-izquierda
        t = lum * .38 + rnd.uniform(-.1, .1)
        col = mix(base, t)
        s += f'<polygon points="{p[0]:.1f},{p[1]:.1f} {q[0]:.1f},{q[1]:.1f} {top[0]:.1f},{top[1]:.1f}" fill="{col}" stroke="{col}" stroke-width=".8"/>'
        if spec and lum > .55 and rnd.random() < .7:
            s += f'<polygon points="{p[0]:.1f},{p[1]:.1f} {q[0]:.1f},{q[1]:.1f} {top[0]:.1f},{top[1]:.1f}" fill="{spec}" opacity=".35"/>'
    return s, pts
def escena(body, glow="#2C5AA0", fondo=("#17315E", "#050B17"), extra=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img">
<defs><radialGradient id="bg" cx=".5" cy=".42" r=".75"><stop offset="0" stop-color="{fondo[0]}"/><stop offset="1" stop-color="{fondo[1]}"/></radialGradient>
<radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{glow}" stop-opacity=".65"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
<linearGradient id="pi" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0A1426" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></linearGradient>
<filter id="bl"><feGaussianBlur stdDeviation="9"/></filter></defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/><ellipse cx="320" cy="250" rx="300" ry="170" fill="url(#gl)"/>
<ellipse cx="320" cy="358" rx="250" ry="30" fill="#000" opacity=".55" filter="url(#bl)"/>{extra}{body}
<rect y="300" width="{W}" height="140" fill="url(#pi)"/></svg>'''
def guardar(n, s): open(os.path.join(OUT, n + ".svg"), "w").write(s)
rnd = random.Random(11)
# CARBÓN
b = ""
for cx, cy, r, c in [(200, 335, 78, "#1A1E26"), (330, 345, 92, "#232833"), (455, 335, 74, "#171A21"), (265, 270, 70, "#2A303C"), (390, 262, 76, "#1E232C"), (330, 195, 66, "#2F3644"), (180, 255, 50, "#20252E"), (470, 255, 52, "#262C37")]:
    s, _ = chunk(cx, cy, r, c, rnd, n=10, spec="#9FB6D9"); b += s
guardar("carbon", escena(b, glow="#3E6FB5"))
# MINERALES
b = ""
for cx, cy, r, c in [(190, 335, 80, "#5B6B80"), (330, 342, 92, "#7C8CA2"), (468, 335, 76, "#B05A30"), (260, 262, 68, "#3F4C5E"), (395, 258, 74, "#8FA0B7"), (335, 192, 60, "#A9B8CC"), (470, 258, 46, "#C46A38")]:
    s, pts = chunk(cx, cy, r, c, rnd, n=9, spec="#FFFFFF"); b += s
    for _ in range(9):
        x = cx + rnd.uniform(-r * .6, r * .6); y = cy + rnd.uniform(-r * .5, r * .2)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.choice([2,3,4])}" fill="#F0C75A"/><circle cx="{x-1:.0f}" cy="{y-1:.0f}" r="1.2" fill="#FFF3C4"/>'
guardar("minerales", escena(b, glow="#4F7FC0"))
# CONSTRUCCIÓN
b = ""
for i in range(120):
    x = rnd.uniform(60, 330); alt = 345 - max(0, 190 - abs(x - 195) * 1.2) * rnd.random()
    s, _ = chunk(x, min(alt, 350), rnd.uniform(11, 20), rnd.choice(["#8E96A3", "#A9B0BB", "#737C8A", "#BFC5CE", "#9AA2AE"]), rnd, n=6); b += s
def bloque(x, y, w, h, c):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/><rect x="{x}" y="{y}" width="{w}" height="{h*.16:.0f}" fill="#fff" opacity=".28"/><rect x="{x}" y="{y+h*.84:.0f}" width="{w}" height="{h*.16:.0f}" fill="#000" opacity=".22"/>'
    for k in range(3): s += f'<rect x="{x+w*(.1+.3*k):.0f}" y="{y+h*.3:.0f}" width="{w*.18:.0f}" height="{h*.4:.0f}" fill="#000" opacity=".35"/>'
    return s
b += bloque(360, 285, 190, 70, "#B9B4A8") + bloque(395, 220, 150, 66, "#CBC7BC")
s, _ = chunk(330, 340, 42, "#F4F2EC", rnd, n=7, spec="#FFFFFF"); b += s
guardar("construccion", escena(b, glow="#5B86C6"))
# ALUMINIO
b = ""
def barra(x, y, w, h):
    g = f'<linearGradient id="g{y}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".18" stop-color="#E4EAF1"/><stop offset=".5" stop-color="#9BA8BA"/><stop offset=".72" stop-color="#D5DCE6"/><stop offset="1" stop-color="#6E7C90"/></linearGradient>'
    return g + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#g{y})"/><rect x="{x}" y="{y+3}" width="{w}" height="3" fill="#fff" opacity=".85"/><rect x="{x+w}" y="{y}" width="26" height="{h}" fill="#5F6D82"/><rect x="{x+w+5}" y="{y+6}" width="16" height="{h-12}" fill="#0E1829" opacity=".85"/>'
b += barra(70, 175, 270, 50) + barra(90, 238, 270, 50) + barra(110, 301, 250, 44)
b += '<radialGradient id="co" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#2B3647"/><stop offset=".22" stop-color="#EEF2F7"/><stop offset=".55" stop-color="#AEB9C8"/><stop offset=".8" stop-color="#E3E8EF"/><stop offset="1" stop-color="#76849A"/></radialGradient>'
b += '<circle cx="500" cy="262" r="104" fill="url(#co)"/>'
for r in range(28, 104, 8): b += f'<circle cx="500" cy="262" r="{r}" fill="none" stroke="#fff" stroke-opacity=".30" stroke-width="1.2"/><circle cx="500" cy="262" r="{r+4}" fill="none" stroke="#3B485B" stroke-opacity=".25" stroke-width="1"/>'
b += '<circle cx="500" cy="262" r="26" fill="#0E1829"/><circle cx="500" cy="262" r="26" fill="none" stroke="#9AA8BA" stroke-width="3"/>'
guardar("aluminio", escena(b, glow="#5C8AD0"))
print("ok")
