# -*- coding: utf-8 -*-
"""Contenido del sitio de la CCMCAIT. Cada página es un bloque de HTML.
Enlaces internos: {{u:slug}}  ·  Archivos de assets: {{a}}archivo
Cifras auditadas el 11 de octubre de 2026 (ver Auditoría en el proyecto)."""

SITIO = {
    "dominio": "https://www.ccmcait.org/",
    "whatsapp": "573164683277",
    "correo": "presidencia@ccmcait.org",
}

# Menú principal (destino, etiqueta)
NAV = [
    ("", "Inicio"),
    ("sobre-la-camara", "La Cámara"),
    ("servicios", "Servicios"),
    ("commodities", "Commodities"),
    ("cobertura", "Cobertura"),
    ("portal-de-oportunidades", "Oportunidades"),
    ("eventos", "Eventos"),
    ("contacto", "Contacto"),
]

# URL vieja -> URL nueva (para no perder enlaces indexados por Google)
REDIRECCIONES = {
    "somos-un-hub-internacional": "como-lo-hacemos",
    "inicio-2": "",
}

WA = "https://wa.me/573164683277?text="

def cta(titulo, texto, boton, destino="contacto", wa_texto="Hola%2C%20quiero%20hablar%20con%20la%20C%C3%A1mara"):
    return f"""<section class="seccion marina"><div class="envoltura"><div class="encabezado-seccion">
<h2>{titulo}</h2><p class="lead">{texto}</p></div>
<div class="acciones"><a class="boton oro" href="{{{{u:{destino}}}}}">{boton}</a><a class="boton sec" href="{WA}{wa_texto}">Escribir por WhatsApp</a></div>
</div></section>"""

def heroe_interior(ante, titulo, lead):
    return f"""<section class="heroe interior"><div class="envoltura"><div class="copia">
<p class="ante">{ante}</p><h1>{titulo}</h1><p class="lead">{lead}</p></div></div></section>"""

DECLARACION = """<div class="declaracion"><div class="marca-sello" aria-hidden="true">SIN<br>INTER-<br>MEDIA-<br>RIOS</div>
<div class="texto"><h3>La Cámara no trabaja con intermediarios</h3>
<p>La CCMCAIT recibe, asesora y orienta directamente a los empresarios. Antes de abrir una puerta, verificamos a cada empresa: autenticidad, registro local, antecedentes judiciales e interés comercial real con las Antillas. Así protegemos a quien compra, a quien vende y a los gobiernos que nos reciben.</p></div></div>"""

EXPORTACIONES = [
    ("República Dominicana", 606.2), ("Jamaica", 177.5), ("Bahamas", 150.8), ("Cuba", 105.8),
    ("Trinidad y Tobago", 55.6), ("San Vicente y las Granadinas", 52.3), ("Aruba", 38.7),
    ("Curazao", 30.7), ("Haití", 28.7), ("Islas Caimán", 15.5), ("Barbados", 12.2),
    ("Turcas y Caicos", 4.7), ("Santa Lucía", 2.5), ("Antigua y Barbuda", 2.1), ("Dominica", 1.6),
    ("Granada", 1.0), ("San Cristóbal y Nieves", 0.6), ("Islas Vírgenes Británicas", 0.2),
]

def num(v):
    return f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")

def barras():
    mx = max(v for _, v in EXPORTACIONES)
    filas = "".join(
        f'<div class="barra" role="listitem"><span>{n}</span><span class="pista"><i style="width:{max(v / mx * 100, 0.6):.1f}%"></i></span><span class="v">{num(v)}</span></div>'
        for n, v in EXPORTACIONES)
    return f'<div class="barras" role="list" aria-label="Exportaciones de Colombia por destino, millones de USD">{filas}</div>'

# ------------------------------------------------------------------ INICIO
INICIO = f"""
<section class="heroe"><div class="envoltura">
<div class="copia">
<p class="ante">Colombia · Caribe · Antillas</p>
<h1>Abrimos puertas entre Colombia y el Caribe</h1>
<p class="lead">Somos el puente institucional para hacer negocios entre Colombia y 34 países y territorios del Caribe y las Antillas: verificamos a las empresas, articulamos con gobiernos y cámaras, y acompañamos cada negocio hasta el cierre.</p>
<div class="acciones"><a class="boton" href="{{{{u:contacto}}}}">Solicitar acompañamiento</a><a class="boton sec" href="{{{{u:servicios}}}}">Ver servicios</a></div>
</div>
<img class="sello" src="{{{{a}}}}emblema.png" alt="Emblema de la CCMCAIT: mapa del Caribe rodeado por las banderas de los países y territorios de cobertura" width="400" height="394">
</div></section>

<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Elija su puerta</p><h2>¿Hacia dónde va su negocio?</h2></div>
<div class="puertas">
<div class="puerta"><p class="ante">Empresas colombianas</p><h3>Quiero llevar mi empresa al Caribe</h3>
<ul><li>Lectura del mercado de destino con datos verificables</li><li>Contactos con compradores, distribuidores y gobiernos</li><li>Acompañamiento en logística y exportación hasta el cierre</li></ul>
<div class="acciones"><a class="boton" href="{{{{u:contacto}}}}">Quiero exportar</a></div></div>
<div class="puerta dos"><p class="ante">Empresas del Caribe y las Antillas</p><h3>Quiero comprar o invertir en Colombia</h3>
<ul><li>Proveedores colombianos verificados por la Cámara</li><li>Agendas con gremios, regiones y entidades de gobierno</li><li>Oportunidades de inversión con respaldo institucional</li></ul>
<div class="acciones"><a class="boton sec" href="{{{{u:portal-de-oportunidades}}}}">Explorar oportunidades</a></div></div>
</div></div></section>

<section class="seccion blanca"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">La región en cifras</p><h2>Un mercado que crece y que Colombia apenas empieza a atender</h2></div>
<div class="cifras">
<div class="cifra"><b>35 M</b><span>llegadas de turistas al Caribe en 2025</span><span class="fuente">Caribbean Tourism Organization</span></div>
<div class="cifra"><b>+23,7 %</b><span>creció la llegada de viajeros suramericanos en 2025</span><span class="fuente">CTO, 2025</span></div>
<div class="cifra"><b>USD 1.287 M</b><span>exportó Colombia a 18 mercados del Caribe en 2025</span><span class="fuente">ONU COMTRADE</span></div>
<div class="cifra"><b>34</b><span>países y territorios en nuestra cobertura</span><span class="fuente">13 países · 21 dependencias</span></div>
</div></div></section>

<section class="seccion"><div class="envoltura columnas">
<div class="texto"><p class="ante">Exportaciones de Colombia al Caribe</p><h2>USD 1.287 millones en 2025</h2>
<p>Esto es lo que Colombia vende hoy a los países y territorios donde trabaja la Cámara. República Dominicana concentra casi la mitad; el resto del Caribe sigue siendo, en su mayoría, un mercado por abrir.</p>
<p class="fuente">Millones de USD. Fuente: ONU COMTRADE vía Trading Economics, datos 2025 (Trinidad y Tobago, Curazao, Turcas y Caicos, Santa Lucía e Islas Vírgenes Británicas: 2024). Puerto Rico, las dependencias francesas y Sint Maarten se reportan dentro de Estados Unidos, Francia y Países Bajos.</p></div>
{barras()}
</div></section>

<section class="seccion blanca"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Qué hacemos</p><h2>Del primer contacto al cierre del negocio</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>Exportación</h3><p>Apertura de mercados, contactos comerciales y acompañamiento logístico hasta el cierre.</p><a class="enlace" href="{{{{u:servicios}}}}">Ver los siete pilares →</a></div>
<div class="tarjeta"><h3>Inversión y alianzas</h3><p>Conexión con socios, gobiernos y cámaras del Caribe para crecer con respaldo institucional.</p><a class="enlace" href="{{{{u:como-lo-hacemos}}}}">Cómo lo hacemos →</a></div>
<div class="tarjeta"><h3>Turismo y gastronomía</h3><p>Promoción de destinos, rutas y oferta colombiana en una región que recibe 35 millones de visitantes al año.</p><a class="enlace" href="{{{{u:eventos}}}}">Agenda de eventos →</a></div>
<div class="tarjeta"><h3>Innovación y educación</h3><p>Tecnología, formación y transferencia de conocimiento entre Colombia y las islas.</p><a class="enlace" href="{{{{u:servicios}}}}">Ver servicios →</a></div>
</div></div></section>

<section class="seccion"><div class="envoltura">{DECLARACION}</div></section>

<section class="seccion blanca"><div class="envoltura columnas">
<div class="texto"><p class="ante">Caso de éxito</p><h2>De Colombia a cinco mercados de la región</h2>
<p>Una compañía colombiana de ciberseguridad y control de acceso, acompañada por la Cámara, ya presta servicios en Panamá, República Dominicana, México y Ecuador, y está abriendo su quinto mercado en Trinidad y Tobago.</p>
<div class="acciones"><a class="boton" href="{{{{u:casos-de-exito}}}}">Ver casos y fichas de país</a></div></div>
<div class="texto"><p class="ante">Respaldo institucional</p><h2>Articulados con quienes abren las puertas</h2>
<p>Hacemos parte de la red de cámaras binacionales y multilaterales que operan en Colombia, con articulación activa con la Presidencia de la República, la Cancillería, las embajadas, el Ministerio de Comercio, Industria y Turismo y las gobernaciones.</p>
<a class="enlace" href="{{{{u:tratados}}}}">Marco multilateral: AEC, CARICOM y OEACP →</a></div>
</div></section>
""" + cta("¿Su empresa quiere llegar al Caribe?", "Cuéntenos qué vende y a qué mercado quiere llegar. Le respondemos con una ruta concreta.", "Hablemos de su negocio")

# ------------------------------------------------------------------ SOBRE
SOBRE = heroe_interior("Quiénes somos", "Sobre la Cámara", "La Cámara de Comercio Multilateral Colombo Antillana de Integración y Turismo (CCMCAIT) es una organización sin ánimo de lucro que conecta al sector empresarial colombiano con los mercados del Caribe y las Antillas.") + f"""
<section class="seccion"><div class="envoltura columnas">
<div class="tarjeta"><p class="ante">Misión</p><p style="color:var(--tinta)">Desarrollar y gestionar con calidad el acompañamiento en el cierre exitoso de los negocios del sector empresarial colombiano con los países del Caribe y las Antillas. Promovemos el turismo, la gastronomía, la educación y la innovación tecnológica en cada uno de nuestros campos de acción, apalancados en el conocimiento de las instituciones afines y en un equipo humano de excelencia.</p></div>
<div class="tarjeta"><p class="ante">Visión</p><p style="color:var(--tinta)">Ser la cámara líder en Colombia en el desarrollo de negocios con los países del Caribe y las Antillas, diferenciándonos con un sello propio que reafirme nuestros valores y propicie el cierre exitoso de los negocios. Entregamos información confiable, oportuna y de alto valor para que los empresarios tomen las decisiones más acertadas.</p></div>
</div></section>
<section class="seccion blanca"><div class="envoltura">{DECLARACION}</div></section>
<section class="seccion"><div class="envoltura columnas">
<div class="texto"><p class="ante">Articulación institucional</p><h2>Respaldo para abrir puertas</h2>
<p>La CCMCAIT hace parte de la red de cámaras binacionales y multilaterales que operan en Colombia y trabaja de la mano de la Presidencia de la República, la Cancillería, las embajadas, el Ministerio de Comercio, Industria y Turismo y las gobernaciones.</p>
<p>Esa articulación es la que permite que una empresa colombiana llegue a una reunión en el Caribe con respaldo, y que una empresa antillana encuentre en Colombia un interlocutor confiable.</p>
<a class="enlace" href="{{{{u:como-lo-hacemos}}}}">Conozca nuestro modelo de trabajo →</a></div>
<div class="texto"><p class="ante">Presencia</p><h2>Bogotá y Santo Domingo</h2>
<p><b>Bogotá, Colombia.</b> Cra. 63 # 98B-51, oficina 204.</p>
<p><b>Santo Domingo, República Dominicana.</b> Av. Los Próceres, Diamond Mall, local 48, Arroyo Hondo.</p>
<p><a href="https://www.youtube.com/watch?v=T09EHZnLUP0">Ver el video institucional en YouTube →</a></p></div>
</div></section>
""" + cta("¿Quiere un acompañamiento como el de nuestros casos?", "Cuéntenos su proyecto y le proponemos una ruta para llegar al Caribe.", "Solicitar acompañamiento")

# ------------------------------------------------------------------ CÓMO LO HACEMOS (+ hub)
COMO = heroe_interior("Modelo de trabajo", "Cómo lo hacemos", "Articulamos oportunidades de negocio integrando a cuatro actores del ecosistema: instituciones y gremios, gobierno, academia y empresarios. Esa red convierte a la Cámara en un hub internacional entre Colombia y el Caribe.") + f"""
<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Los cuatro pilares</p><h2>Una red que trabaja para su negocio</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>Instituciones y gremios</h3><p>Cámaras de comercio, fundaciones e instituciones aliadas que fortalecen la base empresarial.</p></div>
<div class="tarjeta"><h3>Gobierno</h3><p>Presidencia de la República, Cancillería, embajadas, Ministerio de Comercio y gobernaciones, que dan el marco institucional y la cooperación internacional.</p></div>
<div class="tarjeta"><h3>Academia</h3><p>Universidades y centros de formación que aportan conocimiento técnico, investigación y capacitación empresarial.</p></div>
<div class="tarjeta"><h3>Empresarios</h3><p>Quienes generan los negocios, las alianzas comerciales y las oportunidades en los mercados internacionales.</p></div>
</div></div></section>
<section class="seccion blanca"><div class="envoltura columnas">
<div class="texto"><p class="ante">El recorrido de una empresa</p><h2>Así acompañamos cada negocio</h2>
<p>El orden importa: nadie llega a una mesa de negocios en el Caribe sin haber pasado por la verificación de la Cámara.</p></div>
<div class="pasos">
<div class="paso"><h3>Primer contacto</h3><p>Nos cuenta qué vende o qué busca y en qué mercado.</p></div>
<div class="paso"><h3>Verificación</h3><p>Validamos registro local, trayectoria, antecedentes judiciales e interés comercial real.</p></div>
<div class="paso"><h3>Lectura del mercado</h3><p>Preparamos la información del país de destino con datos verificables.</p></div>
<div class="paso"><h3>Conexión institucional</h3><p>Activamos la red: cámaras, gremios, gobiernos y contrapartes en el país.</p></div>
<div class="paso"><h3>Acompañamiento al cierre</h3><p>Seguimos el proceso, incluida la logística con operadores aliados, hasta cerrar el negocio.</p></div>
</div></div></section>
<section class="seccion"><div class="envoltura texto">
<p class="ante">Red de Cámaras Binacionales</p><h2>Conectados con mercados globales</h2>
<p>La Cámara forma parte de la Red de Cámaras Binacionales y participa en encuentros, espacios de networking y congresos internacionales que fortalecen la cooperación empresarial. A través de esta red consolida alianzas con organizaciones de distintos países y promueve oportunidades de negocio e intercambio de conocimiento.</p>
</div></section>
""" + cta("Ponga a trabajar esta red para su empresa", "El primer paso es una conversación con la Cámara.", "Solicitar acompañamiento")

# ------------------------------------------------------------------ TRATADOS
TRATADOS = heroe_interior("Marco multilateral", "Tratados y organismos", "La CCMCAIT promueve el relacionamiento con los organismos de integración regional que dan reglas, acceso y cooperación al comercio entre Colombia y el Caribe.") + f"""
<section class="seccion"><div class="envoltura rejilla">
<div class="tarjeta"><p class="ante">Asociación de Estados del Caribe</p><h3>AEC</h3>
<p>Su convenio constitutivo se firmó el 24 de julio de 1994 en Cartagena de Indias, Colombia, para promover la consulta, la cooperación y la acción concertada entre los países del Gran Caribe. Trabaja en comercio, turismo sostenible, transporte y gestión de riesgos.</p>
<p><b>Para el empresario:</b> es el espacio regional donde Colombia participa como miembro, lo que facilita el diálogo con los gobiernos del Caribe.</p>
<a class="enlace" href="https://www.acs-aec.org/es">acs-aec.org →</a></div>
<div class="tarjeta"><p class="ante">Comunidad del Caribe</p><h3>CARICOM</h3>
<p>Creada en 1973, agrupa a 15 Estados miembros y 6 miembros asociados. Impulsa el Mercado y Economía Única del Caribe (CSME), que busca libre circulación de bienes, servicios, capitales y personas entre sus miembros.</p>
<p><b>Para el empresario:</b> un producto que entra a un país de CARICOM puede proyectarse hacia un mercado regional integrado.</p>
<a class="enlace" href="https://caricom.org/">caricom.org →</a></div>
<div class="tarjeta"><p class="ante">Antes Grupo ACP</p><h3>OEACP</h3>
<p>La Organización de Estados de África, el Caribe y el Pacífico nació en 1975 con el Acuerdo de Georgetown y en abril de 2020 pasó de ser el Grupo ACP a organización internacional. Reúne 79 Estados y mantiene acuerdos de asociación con la Unión Europea.</p>
<p><b>Para el empresario:</b> los países caribeños de la OEACP tienen acceso preferente a Europa, lo que abre rutas de triangulación comercial.</p>
<a class="enlace" href="https://www.oacps.org/">oacps.org →</a></div>
</div></section>
""" + cta("¿Quiere saber qué acuerdo aplica a su producto?", "Le orientamos según el país de destino.", "Consultar a la Cámara")

# ------------------------------------------------------------------ ALIADOS
ALIADOS = heroe_interior("Alianzas", "Aliados estratégicos", "La CCMCAIT articula alianzas con empresas, instituciones y proyectos que fortalecen la integración comercial entre Colombia y la región. Cada alianza pasa por la misma evaluación de viabilidad y pertinencia.") + f"""
<section class="seccion"><div class="envoltura rejilla">
<div class="tarjeta"><p class="ante">Detailing automotriz</p><h3>Margrey</h3><p>Productos especializados de detailing automotriz con proyección internacional, disponibles para procesos de distribución y expansión en mercados del Caribe.</p></div>
<div class="tarjeta"><p class="ante">Proyecto en desarrollo</p><h3>FOL</h3><p>Iniciativa para estructurar oportunidades comerciales y logísticas en la región, conectando proveedores con mercados estratégicos.</p></div>
<div class="tarjeta"><p class="ante">Para empresarios</p><h3>Valor de las alianzas</h3><p>Acceso a oportunidades reales de negocio y participación en procesos de expansión internacional con respaldo de la Cámara.</p></div>
</div></section>
""" + cta("¿Su institución o empresa quiere ser aliada?", "Conversemos sobre cómo articularnos.", "Quiero ser aliado", wa_texto="Hola%2C%20quiero%20ser%20aliado%20estrat%C3%A9gico")

# ------------------------------------------------------------------ SERVICIOS
PILARES = [
    ("Industria", "Textil, construcción (tuberías, ladrillos, sistemas hidráulicos y eléctricos), insumos médicos, repuestos automotrices, carrocerías para buses e insumos industriales como acero, combustibles y químicos."),
    ("Proceso de exportación", "Alianzas con operadores logísticos y portuarios para gestionar su exportación hacia el Caribe, con acompañamiento en logística internacional de principio a fin."),
    ("Educación", "Alianzas con universidades, capacitación en modelos de exportación por regiones, formación empresarial e integración con entidades de gobierno para acceder a beneficios."),
    ("Deporte", "Promoción de actividades deportivas y asesoría en lineamientos del sector, como puente adicional de relacionamiento entre Colombia y el Caribe."),
    ("Tecnología y consultoría", "Energías eólica y solar, telecomunicaciones, sistemas de gestión, consultoría ambiental, economía circular, manejo de residuos y construcción sostenible."),
    ("Alimentos, agricultura y ganadería", "Productos agrícolas y alimenticios, insumos para la industria alimentaria, bebidas y producción ganadera, pesquera, avícola y porcícola."),
    ("Proyectos especiales", "Proyectos de construcción, educativos, deportivos, ambientales, interinstitucionales y de gobierno."),
]
tarjetas_pilares = "".join(
    f'<div class="tarjeta"><h3>{n}</h3><p>{t}</p><a class="enlace" href="{WA}Hola%2C%20me%20interesa%20el%20pilar%20{n.replace(" ", "%20").replace(",", "%2C").replace("ó", "%C3%B3").replace("í", "%C3%AD").replace("é", "%C3%A9")}">Consultar este pilar →</a></div>'
    for n, t in PILARES)
SERVICIOS = heroe_interior("Servicios", "Siete pilares para crecer en el Caribe", "La CCMCAIT acompaña a los empresarios en siete sectores estratégicos para desarrollar negocios entre Colombia y los mercados del Caribe y las Antillas.") + f"""
<section class="seccion"><div class="envoltura rejilla">{tarjetas_pilares}
<div class="tarjeta" style="border-color:var(--oro)"><h3>¿No encuentra su sector?</h3><p>Escríbanos y lo ubicamos en el pilar correcto.</p><a class="enlace" href="{{{{u:contacto}}}}">Hablar con la Cámara →</a></div>
</div></section>
""" + cta("Llevemos su empresa al Caribe", "Le acompañamos desde el primer contacto hasta el cierre del negocio.", "Quiero empezar")

# ------------------------------------------------------------------ COBERTURA
PAISES = [
    ("Antigua y Barbuda", "ATG", "https://ab.gov.ag/"), ("Bahamas", "BHS", "https://www.bahamas.gov.bs/"),
    ("Barbados", "BRB", "https://www.gov.bb/"), ("Cuba", "CUB", "https://www.presidencia.gob.cu/es/"),
    ("Dominica", "DMA", "https://dominica.gov.dm/"), ("Granada", "GRD", "https://www.gov.gd/"),
    ("Haití", "HTI", "https://www.primature.gouv.ht/"), ("Jamaica", "JAM", "https://www.gov.jm/"),
    ("República Dominicana", "DOM", "https://www.presidencia.gob.do/"), ("San Cristóbal y Nieves", "KNA", "https://www.gov.kn/"),
    ("San Vicente y las Granadinas", "VCT", "https://www.gov.vc/"), ("Santa Lucía", "LCA", "https://www.govt.lc/"),
    ("Trinidad y Tobago", "TTO", "https://www.ttconnect.gov.tt/"),
]
DEPENDENCIAS = [
    ("Estados Unidos", [("Puerto Rico", "https://pr.gov/"), ("Islas Vírgenes de EE. UU.", None), ("Isla de Navaza", None)]),
    ("Francia", [("Guadalupe", "https://www.regionguadeloupe.fr/"), ("Martinica", "https://www.martinique.gouv.fr/"), ("San Bartolomé", "https://www.comstbarth.fr/"), ("San Martín", "https://www.saint-barth-saint-martin.gouv.fr/")]),
    ("Reino de los Países Bajos", [("Aruba", None), ("Bonaire", None), ("Curazao", None), ("Saba", None), ("San Eustaquio", None), ("Sint Maarten", "https://www.sintmaartengov.org/")]),
    ("Reino Unido", [("Islas Caimán", "https://www.gov.ky/"), ("Islas Turcas y Caicos", None), ("Islas Vírgenes Británicas", None), ("Anguila", "https://www.gov.ai/"), ("Montserrat", "https://www.gov.ms/")]),
    ("Venezuela", [("Dependencias Federales", None), ("Nueva Esparta", None)]),
    ("Colombia", [("San Andrés, Providencia y Santa Catalina", "https://www.sanandres.gov.co/")]),
]
def li(nombre, enlace, extra=""):
    n = f'<a href="{enlace}">{nombre}</a>' if enlace else nombre
    return f"<li><span>{n}</span>{extra}</li>"
lista_paises = "".join(li(n, e, f'<span class="iso">{iso}</span>') for n, iso, e in PAISES)
grupos_dep = "".join(f'<div class="grupo"><p class="ante">{s}</p><ul>{"".join(li(n, e) for n, e in t)}</ul></div>' for s, t in DEPENDENCIAS)
COBERTURA = heroe_interior("Cobertura geográfica", "34 países y territorios del Caribe y las Antillas", "La CCMCAIT desarrolla actividades en 13 países soberanos y 21 dependencias administradas por Estados Unidos, Francia, el Reino de los Países Bajos, el Reino Unido, Venezuela y Colombia.") + f"""
<section class="seccion"><div class="envoltura columnas">
<div class="grupo"><p class="ante">13 países soberanos</p><h3>Estados del Caribe</h3><ul>{lista_paises}</ul><p class="fuente">Cada nombre enlaza al portal oficial de su gobierno.</p></div>
<div class="texto"><p class="ante">Por qué importa</p><h2>Un mismo mar, seis sistemas jurídicos</h2>
<p>Cada territorio tiene su propia aduana, su moneda y sus reglas de entrada. La isla de San Martín, por ejemplo, está dividida entre Francia y el Reino de los Países Bajos. La Cámara le orienta sobre el marco que aplica en cada destino antes de que su producto viaje.</p>
<a class="boton" href="{{{{u:contacto}}}}" style="justify-self:start">Consultar un mercado</a></div>
</div></section>
<section class="seccion blanca"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">21 dependencias</p><h2>Territorios por Estado administrador</h2></div>
<div class="territorios">{grupos_dep}</div></div></section>
""" + cta("¿A qué mercado quiere llegar?", "Le preparamos la lectura del país con datos verificables.", "Solicitar información")

# ------------------------------------------------------------------ PORTAL
PORTAL = heroe_interior("Portal de oportunidades", "Donde la oferta y la demanda del Caribe se encuentran", "Un directorio de oportunidades comerciales por sector. Ninguna oportunidad se publica sin pasar antes por la verificación institucional de la Cámara.") + f"""
<section class="seccion"><div class="envoltura puertas">
<div class="puerta"><p class="ante">Empresas colombianas</p><h3>Vender en el Caribe</h3><p>Registre su oferta y reciba solicitudes verificadas de compradores en los mercados que cubrimos.</p>
<div class="acciones"><a class="boton" href="{{{{u:contacto}}}}">Publicar una oportunidad</a></div></div>
<div class="puerta dos"><p class="ante">Empresas del Caribe y las Antillas</p><h3>Comprar o invertir en Colombia</h3><p>Acceda a proveedores, socios y oportunidades de inversión colombianas con respaldo institucional.</p>
<div class="acciones"><a class="boton sec" href="{{{{u:contacto}}}}">Solicitar proveedores</a></div></div>
</div></section>
<section class="seccion blanca"><div class="envoltura columnas">
<div class="texto"><p class="ante">Cómo garantizamos la calidad</p><h2>Verificación institucional</h2><p>Antes de publicar una oportunidad o presentar una contraparte, la Cámara revisa cuatro puntos.</p></div>
<div class="pasos">
<div class="paso"><h3>Registro local</h3><p>La empresa está legalmente registrada en su país.</p></div>
<div class="paso"><h3>Trayectoria</h3><p>Historial y capacidad comercial demostrables.</p></div>
<div class="paso"><h3>Antecedentes</h3><p>Revisión de antecedentes judiciales de la empresa.</p></div>
<div class="paso"><h3>Interés genuino</h3><p>Confirmamos el interés comercial real antes de presentar a las partes.</p></div>
</div></div></section>
<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Sectores</p><h2>Oportunidades por pilar</h2><p class="lead">El directorio se organiza según los siete pilares de la Cámara.</p></div>
<div class="rejilla">{"".join(f'<div class="tarjeta"><h3>{n}</h3><a class="enlace" href="{WA}Hola%2C%20busco%20oportunidades%20en%20{n.split(",")[0].replace(" ", "%20").replace("ó", "%C3%B3").replace("í", "%C3%AD")}">Consultar oportunidades →</a></div>' for n, _ in PILARES)}</div>
</div></section>
""" + cta("¿Tiene una oportunidad para el Caribe?", "Publíquela con el respaldo de la Cámara y conecte con compradores verificados.", "Publicar oportunidad")

# ------------------------------------------------------------------ CASOS
CASOS = heroe_interior("Casos de éxito", "La confianza se construye con datos", "Cada ficha de país resume qué importa ese mercado, de dónde y cuánto le compra hoy a Colombia. Es la base para encontrar la oportunidad real.") + f"""
<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Ficha de país · 2025</p><h2>Barbados</h2><p class="lead">Barbados importó USD 2.290 millones en 2025. De Colombia compró USD 12,2 millones, apenas el 0,5 %.</p></div>
<div class="cifras">
<div class="cifra"><b>USD 2.290 M</b><span>importaciones totales</span></div>
<div class="cifra"><b>USD 400 M+</b><span>en alimentos y bebidas</span></div>
<div class="cifra"><b>USD 12,2 M</b><span>compras a Colombia</span></div>
<div class="cifra"><b>0,5 %</b><span>participación de Colombia</span></div>
</div></div></section>
<section class="seccion blanca"><div class="envoltura columnas">
<div><h3 style="margin-bottom:14px">De dónde importa Barbados</h3>
<div class="tabla-envoltura"><table><thead><tr><th>Origen</th><th style="text-align:right">Millones USD</th></tr></thead><tbody>
<tr><td>Estados Unidos</td><td class="num">869,2</td></tr><tr><td>Trinidad y Tobago</td><td class="num">355,9</td></tr><tr><td>China</td><td class="num">178,2</td></tr><tr><td>Países Bajos</td><td class="num">133,1</td></tr><tr><td>Reino Unido</td><td class="num">106,7</td></tr><tr><td>Colombia</td><td class="num">12,2</td></tr>
</tbody></table></div></div>
<div><h3 style="margin-bottom:14px">Alimentos y bebidas que compra</h3>
<div class="tabla-envoltura"><table><thead><tr><th>Capítulo</th><th style="text-align:right">Millones USD</th></tr></thead><tbody>
<tr><td>Bebidas</td><td class="num">60,3</td></tr><tr><td>Lácteos, huevos y miel</td><td class="num">53,3</td></tr><tr><td>Carnes</td><td class="num">49,7</td></tr><tr><td>Preparaciones alimenticias</td><td class="num">48,1</td></tr><tr><td>Cereales y preparaciones</td><td class="num">38,3</td></tr><tr><td>Conservas de frutas y hortalizas</td><td class="num">35,7</td></tr><tr><td>Frutas</td><td class="num">35,1</td></tr><tr><td>Pescados y mariscos</td><td class="num">30,5</td></tr><tr><td>Hortalizas</td><td class="num">24,9</td></tr><tr><td>Preparaciones de carne y pescado</td><td class="num">24,8</td></tr>
</tbody></table></div></div>
</div>
<div class="envoltura" style="margin-top:28px"><div class="aviso"><b>Lectura comercial.</b> Barbados compra más de USD 400 millones al año en alimentos y bebidas, categorías en las que Colombia compite en costo y calidad. La distancia entre ese mercado y los USD 12,2 millones que hoy le vende Colombia es la oportunidad.</div>
<p class="fuente" style="margin-top:12px">Fuente: ONU COMTRADE vía Trading Economics, datos 2025. Consultado el 11 de octubre de 2026.</p></div>
</section>
<section class="seccion"><div class="envoltura columnas">
<div class="texto"><p class="ante">Acompañamiento</p><h2>Ciberseguridad colombiana en cinco mercados</h2>
<p>Una compañía colombiana especializada en ciberseguridad y control de acceso, acompañada por la Cámara, presta servicios en Panamá, República Dominicana, México y Ecuador, y está en proceso de apertura en Trinidad y Tobago.</p></div>
<div class="tabla-envoltura"><table><thead><tr><th>Mercado</th><th>Estado</th></tr></thead><tbody>
<tr><td>Panamá</td><td>En operación</td></tr><tr><td>República Dominicana</td><td>En operación</td></tr><tr><td>México</td><td>En operación</td></tr><tr><td>Ecuador</td><td>En operación</td></tr><tr><td>Trinidad y Tobago</td><td>En apertura</td></tr>
</tbody></table></div>
</div></section>
""" + cta("¿Qué mercado quiere explorar?", "Le preparamos la ficha de su país de interés con datos verificables.", "Quiero mi ficha")

# ------------------------------------------------------------------ EVENTOS
# Agenda: (fecha visible, lugar, título, descripción, sector, enlace, en Colombia, último día AAAA-MM-DD).
# Los eventos cuyo último día ya pasó no se generan, y en la página publicada se ocultan solos.
EVENTOS_LISTA = [
    ("22–24 oct", "Santo Domingo, R. Dominicana", "Bolsa Turística del Caribe (BTC) 2026", "Hotel El Embajador. Edición de 30 años de la feria de turismo de referencia en República Dominicana.", "Turismo", "https://www.btc.com.do/", False, "2026-10-24"),
    ("16–18 nov", "Barbados", "CHIEF 2026", "Caribbean Hotel & Tourism Association, Wyndham Grand Barbados Sam Lords Castle. Foro de la industria hotelera.", "Turismo y hospitalidad", "https://caribbeanhotelandtourism.com/events/", False, "2026-11-18"),
    ("16–19 nov", "Barbados", "Taste of the Caribbean 2026", "Caribbean Hotel & Tourism Association. Competencia culinaria e intercambio con proveedores de alimentos y bebidas.", "Alimentos y gastronomía", "https://caribbeanhotelandtourism.com/events/", False, "2026-11-19"),
    ("27–29 nov", "Paramaribo, Surinam", "Suriname Tourism & Food Festival 2026", "Torarica Resort. La principal feria de turismo de Surinam.", "Turismo y alimentos", None, False, "2026-11-29"),
]
import datetime as _dt
PROXIMOS = [e for e in EVENTOS_LISTA if e[7] >= _dt.date.today().isoformat()]
def fila_evento(f, lugar, t, d, s, u, co, hasta):
    etiquetas = ('<span class="etiqueta co">En Colombia</span>' if co else "") + f'<span class="etiqueta">{s}</span>'
    enlace = f' <a href="{u}">Sitio del evento →</a>' if u else ""
    return f'<div class="evento" data-hasta="{hasta}"><div class="fecha">{f}<small>{lugar}</small></div><div class="texto" style="gap:6px"><h3>{t}</h3><p>{d}</p><p>{etiquetas}{enlace}</p></div></div>'
filas_eventos = "".join(fila_evento(*e) for e in PROXIMOS)
OCULTAR_PASADOS = """<script>(function(){var hoy=new Date();hoy.setHours(0,0,0,0);var quedan=0;
document.querySelectorAll('.evento[data-hasta]').forEach(function(e){if(new Date(e.dataset.hasta+'T23:59:59')<hoy){e.remove();}else{quedan++;}});
if(!quedan){var a=document.querySelector('.agenda');if(a){a.hidden=true;}var v=document.querySelector('[data-sin-eventos]');if(v){v.hidden=false;}}})();</script>"""

# Actividades de la Cámara, con fotos en src/assets/actividades/:
# (fecha, lugar, título, descripción, [(archivo, texto alternativo, ancho, alto), ...]). La primera foto es la principal.
ACTIVIDADES = []
def foto_actividad(archivo, alt, ancho, alto):
    return f'<a href="{{{{a}}}}actividades/{archivo}"><img src="{{{{a}}}}actividades/{archivo}" alt="{alt}" width="{ancho}" height="{alto}" loading="lazy"></a>'
def tarjeta_actividad(fecha, lugar, titulo, desc, fotos):
    mini = f'<div class="miniaturas">{"".join(foto_actividad(*x) for x in fotos[1:])}</div>' if len(fotos) > 1 else ""
    return f'<article class="actividad"><div class="foto-principal">{foto_actividad(*fotos[0])}</div>{mini}<div class="cuerpo"><p class="ante">{fecha} · {lugar}</p><h3>{titulo}</h3><p>{desc}</p></div></article>'
SECCION_ACTIVIDADES = (f"""
<section class="seccion blanca"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Lo que hemos hecho</p><h2>Actividades de la Cámara</h2><p class="lead">Encuentros, ferias y misiones en las que la CCMCAIT ha representado a los empresarios de Colombia y el Caribe.</p></div>
<div class="actividades">{"".join(tarjeta_actividad(*a) for a in ACTIVIDADES)}</div>
</div></section>""" if ACTIVIDADES else "")

EVENTOS = heroe_interior("Eventos y actividades", "Eventos del Caribe y Colombia", "La CCMCAIT sigue los principales eventos, ferias y encuentros empresariales de la región para que su empresa llegue donde están las oportunidades.") + SECCION_ACTIVIDADES + f"""
<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><p class="ante">Próximos eventos</p><h2>Agenda del Caribe y Colombia</h2></div>
<div class="agenda"{"" if PROXIMOS else " hidden"}>{filas_eventos}</div>
<p class="aviso" data-sin-eventos{" hidden" if PROXIMOS else ""}>Estamos preparando la próxima agenda. Escríbanos y le contamos qué eventos vienen.</p>
<p class="fuente" style="margin-top:14px">Agenda verificada el 11 de octubre de 2026 y actualizada el 22 de octubre de 2026 con las fuentes de cada organizador. Las fechas pueden cambiar; confirme con el organizador antes de viajar.</p>
</div></section>
{OCULTAR_PASADOS}
""" + cta("¿Quiere que su empresa vaya a alguno?", "Le ayudamos a preparar la agenda, los contactos y las reuniones para que cada evento se convierta en negocios.", "Quiero participar")

# ------------------------------------------------------------------ CONTACTO
FORM_ACCION = "https://formsubmit.co/presidencia@ccmcait.org"
CONTACTO = heroe_interior("Contacto", "Hablemos de su negocio en el Caribe", "Nuestro equipo evalúa cada solicitud y le acompaña en todo el proceso. Elija la ruta rápida por WhatsApp o déjenos su proyecto en el formulario.") + f"""
<section class="seccion"><div class="envoltura rejilla">
<div class="tarjeta"><h3>Quiero exportar al Caribe</h3><p>Para empresas colombianas que buscan entrar a un nuevo mercado.</p><a class="enlace" href="{WA}Hola%2C%20quiero%20exportar%20al%20Caribe">Escribir por WhatsApp →</a></div>
<div class="tarjeta"><h3>Quiero importar desde Colombia</h3><p>Para empresas del Caribe y las Antillas interesadas en proveedores colombianos.</p><a class="enlace" href="{WA}Hola%2C%20quiero%20importar%20desde%20Colombia">Escribir por WhatsApp →</a></div>
<div class="tarjeta"><h3>Quiero ser aliado estratégico</h3><p>Para instituciones, gremios y academia interesados en articular con la Cámara.</p><a class="enlace" href="{WA}Hola%2C%20quiero%20ser%20aliado%20estrat%C3%A9gico">Escribir por WhatsApp →</a></div>
</div></section>
<section class="seccion blanca"><div class="envoltura columnas">
<form class="formulario" data-formulario action="{FORM_ACCION}" method="POST">
<h2>Cuéntenos su proyecto</h2>
<input type="hidden" name="_subject" value="Nueva solicitud desde ccmcait.org">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://www.ccmcait.org/gracias/">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="dos-col">
<div class="campo"><label for="nombre">Nombre y apellido *</label><input id="nombre" name="nombre" required autocomplete="name" value=""></div>
<div class="campo"><label for="empresa">Empresa o institución</label><input id="empresa" name="empresa" autocomplete="organization"></div>
<div class="campo"><label for="correo">Correo electrónico *</label><input id="correo" name="email" type="email" required autocomplete="email"></div>
<div class="campo"><label for="telefono">Teléfono / WhatsApp</label><input id="telefono" name="telefono" type="tel" autocomplete="tel"></div>
</div>
<div class="campo"><label for="necesidad">¿Qué necesita? *</label><select id="necesidad" name="necesidad" required><option value="">Seleccione una opción</option><option>Quiero exportar al Caribe</option><option>Quiero importar desde Colombia</option><option>Quiero publicar una oportunidad</option><option>Quiero ser aliado estratégico</option><option>Otro tema</option></select></div>
<div class="campo"><label for="mensaje">Cuéntenos su proyecto *</label><textarea id="mensaje" name="mensaje" rows="5" required placeholder="Qué vende o busca, y en qué país."></textarea></div>
<label class="consentimiento" for="acepto"><input id="acepto" name="autorizacion_datos" type="checkbox" value="Autoriza" required> <span>Autorizo a la CCMCAIT a tratar mis datos para responder esta solicitud, según el <a href="{{{{u:privacidad}}}}">aviso de privacidad</a> (Ley 1581 de 2012).</span></label>
<div><button class="boton" type="submit">Enviar solicitud</button></div>
<p class="aviso" data-nota hidden>Vista previa: en el sitio publicado este formulario llega al correo de la Cámara.</p>
</form>
<div class="texto">
<p class="ante">Canales directos</p><h2>Así puede encontrarnos</h2>
<div class="canales">
<div class="canal"><b>Correo institucional</b><span>presidencia@ccmcait.org</span></div>
<div class="canal"><b>WhatsApp institucional</b><a href="https://wa.me/573164683277">+57 316 468 3277</a></div>
<div class="canal"><b>Bogotá, Colombia</b><span>Cra. 63 # 98B-51, oficina 204</span></div>
<div class="canal"><b>Santo Domingo, R. Dominicana</b><span>Av. Los Próceres, Diamond Mall, local 48, Arroyo Hondo</span></div>
</div></div>
</div></section>
"""

# ------------------------------------------------------------------ PRIVACIDAD
PRIVACIDAD = heroe_interior("Habeas data", "Aviso de privacidad y tratamiento de datos personales", "En cumplimiento de la Ley 1581 de 2012 y el Decreto 1377 de 2013 de la República de Colombia.") + f"""
<section class="seccion"><div class="envoltura texto">
<h3>Responsable del tratamiento</h3><p>Cámara de Comercio Multilateral Colombo Antillana de Integración y Turismo (CCMCAIT), con domicilio en Cra. 63 # 98B-51, oficina 204, Bogotá, Colombia. Correo: presidencia@ccmcait.org. WhatsApp: +57 316 468 3277.</p>
<h3>Datos que recogemos y para qué</h3><p>Nombre, empresa, correo, teléfono y la descripción de su proyecto, que usted entrega en los formularios o por WhatsApp. Los usamos solo para responder su solicitud, verificar a las empresas que se presentan a la Cámara y acompañar sus procesos de negocio. No vendemos ni cedemos sus datos a terceros con fines comerciales.</p>
<h3>Sus derechos</h3><p>Puede conocer, actualizar, rectificar y suprimir sus datos, revocar la autorización y presentar quejas ante la Superintendencia de Industria y Comercio. Para ejercerlos, escriba a presidencia@ccmcait.org; respondemos consultas en un máximo de diez días hábiles y reclamos en un máximo de quince.</p>
<h3>Encargados</h3><p>Los formularios del sitio se transmiten por un servicio de reenvío de correo (FormSubmit) hasta el buzón institucional de la Cámara.</p>
<p class="fuente">Vigente desde octubre de 2026.</p>
</div></section>
"""

GRACIAS = heroe_interior("Solicitud recibida", "Gracias por escribirnos", "Recibimos su solicitud. La Cámara la revisará y le responderá por correo o WhatsApp.") + """
<section class="seccion"><div class="envoltura acciones"><a class="boton" href="{{u:}}">Volver al inicio</a><a class="boton sec" href="{{u:eventos}}">Ver la agenda de eventos</a></div></section>"""

COMMODITIES = heroe_interior("Commodities", "Commodities de Colombia para el Caribe y el mundo", "La CCMCAIT conecta a compradores, importadores y comercializadores con proveedores de carbón, minerales, materiales de construcción y aluminio. Cada proveedor pasa por la verificación de la Cámara antes de ser presentado.") + """
<section class="seccion"><div class="envoltura">
<div class="encabezado-seccion"><h2>Portafolio</h2><p class="lead">Categorías disponibles para consulta. Especificaciones, volúmenes y precios se entregan por solicitud, según el producto y el destino.</p></div>
<div class="rejilla productos">
<article class="tarjeta producto"><img src="{{a}}commodities/carbon.svg" alt="Carbón mineral" width="320" height="220" loading="lazy"><div class="cuerpo-producto"><h3>Carbón</h3><p>Térmico y coquizable.</p></div></article>
<article class="tarjeta producto"><img src="{{a}}commodities/minerales.svg" alt="Minerales metálicos" width="320" height="220" loading="lazy"><div class="cuerpo-producto"><h3>Minerales metálicos</h3><p>Níquel, hierro y ferroaleaciones.</p></div></article>
<article class="tarjeta producto"><img src="{{a}}commodities/construccion.svg" alt="Materiales de construcción" width="320" height="220" loading="lazy"><div class="cuerpo-producto"><h3>Materiales de construcción</h3><p>Cemento, agregados pétreos y yeso.</p></div></article>
<article class="tarjeta producto"><img src="{{a}}commodities/aluminio.svg" alt="Aluminio" width="320" height="220" loading="lazy"><div class="cuerpo-producto"><span class="etiqueta">Programa piloto</span><h3>Aluminio y metales no ferrosos</h3><p>Chatarra, aluminio primario, billet, perfiles extruidos, chapa y bobina.</p></div></article>
</div></div></section>
<section class="seccion blanca"><div class="envoltura">
<div class="encabezado-seccion"><h2>Cómo funciona</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>1. Nos cuenta qué necesita</h3><p>Producto, volumen aproximado y destino de entrega.</p></div>
<div class="tarjeta"><h3>2. Verificamos y cotizamos</h3><p>Presentamos solo proveedores que pasaron la verificación de la Cámara y le enviamos una cotización indicativa.</p></div>
<div class="tarjeta"><h3>3. Acompañamos la operación</h3><p>Contacto institucional, coordinación logística y seguimiento hasta la entrega.</p></div>
</div>
<div class="acciones"><a class="boton sec" href="{{a}}flyer-commodities-es.pdf">Descargar flyer (español)</a><a class="boton sec" href="{{a}}flyer-commodities-en.pdf">Download flyer (English)</a></div>
</div></section>
""" + cta("Cotice sus commodities con la Cámara", "Cuéntenos qué producto busca y a qué destino. Le respondemos por WhatsApp o correo.", "Solicitar cotización", wa_texto="Hola%2C%20quiero%20cotizar%20commodities")

PAGINAS = {
    "": {"titulo": "CCMCAIT | Cámara de Comercio Colombo Antillana", "descripcion": "Puente institucional para hacer negocios entre Colombia y 34 países y territorios del Caribe y las Antillas, con verificación de empresas y respaldo diplomático.", "html": INICIO},
    "sobre-la-camara": {"titulo": "Sobre la Cámara | CCMCAIT", "descripcion": "Misión, visión y articulación institucional de la Cámara de Comercio Multilateral Colombo Antillana de Integración y Turismo.", "html": SOBRE, "hijas": ["como-lo-hacemos", "tratados", "aliados-estrategicos"]},
    "como-lo-hacemos": {"titulo": "Cómo lo hacemos | CCMCAIT", "descripcion": "Modelo de trabajo de la CCMCAIT: instituciones, gobierno, academia y empresarios conectados para cerrar negocios en el Caribe.", "html": COMO},
    "tratados": {"titulo": "Tratados y organismos | CCMCAIT", "descripcion": "AEC, CARICOM y OEACP: el marco multilateral que facilita el comercio entre Colombia y el Caribe.", "html": TRATADOS},
    "aliados-estrategicos": {"titulo": "Aliados estratégicos | CCMCAIT", "descripcion": "Empresas, instituciones y proyectos aliados de la CCMCAIT para la integración comercial Colombia-Caribe.", "html": ALIADOS},
    "servicios": {"titulo": "Servicios | CCMCAIT", "descripcion": "Siete pilares para exportar, importar e invertir entre Colombia y el Caribe: industria, exportación, educación, deporte, tecnología, alimentos y proyectos especiales.", "html": SERVICIOS},
    "cobertura": {"titulo": "Cobertura | CCMCAIT", "descripcion": "Los 13 países y 21 dependencias del Caribe y las Antillas donde trabaja la CCMCAIT, con enlaces a sus gobiernos.", "html": COBERTURA},
    "portal-de-oportunidades": {"titulo": "Portal de oportunidades | CCMCAIT", "descripcion": "Oportunidades de negocio verificadas entre Colombia y el Caribe: vender, comprar e invertir con respaldo de la Cámara.", "html": PORTAL, "hijas": ["casos-de-exito"]},
    "casos-de-exito": {"titulo": "Casos de éxito | CCMCAIT", "descripcion": "Fichas de país con datos verificados y casos de empresas colombianas acompañadas por la Cámara en el Caribe.", "html": CASOS},
    "eventos": {"titulo": "Eventos del Caribe | CCMCAIT", "descripcion": "Próximas ferias, foros y misiones comerciales en el Caribe y Colombia, y actividades de la CCMCAIT.", "html": EVENTOS},
    "commodities": {"titulo": "Commodities | CCMCAIT", "descripcion": "Carbón, minerales, materiales de construcción y aluminio con proveedores verificados por la Cámara, para compradores del Caribe y el mundo.", "html": COMMODITIES},
    "contacto": {"titulo": "Contacto | CCMCAIT", "descripcion": "Escriba a la CCMCAIT para exportar al Caribe, importar desde Colombia o ser aliado estratégico. Oficinas en Bogotá y Santo Domingo.", "html": CONTACTO},
    "privacidad": {"titulo": "Aviso de privacidad | CCMCAIT", "descripcion": "Política de tratamiento de datos personales de la CCMCAIT según la Ley 1581 de 2012.", "html": PRIVACIDAD},
    "gracias": {"titulo": "Solicitud recibida | CCMCAIT", "descripcion": "Gracias por escribir a la CCMCAIT.", "html": GRACIAS, "noindex": True},
}
