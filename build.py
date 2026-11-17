"""Genera la web de Baulat (VAL a l'arrel, CAS a /es/). Edita els textos ací i torna a executar."""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/baulat-site"
DOMAIN = "https://baulat.com"      # canvia-ho pel domini real
EMAIL = "baulat@baulat.com"                     # p. ex. hola@baulat.es
TELEGRAM = "https://t.me/BaulatServicios"    # el teu usuari o bot de contacte

T = {
  "va": {
    "lang": "ca-ES", "prefix": "", "other": "es/",
    "title": "Baulat · Programari xicotet per a consultes xicotetes",
    "desc": "Cites per Telegram, factures des del mòbil i gestió de consulta per a fisios, dentistes, psicòlegs i autònoms. Fet a l'Horta Sud.",
    "skip": "Vés al contingut",
    "nav": ["Eines", "Com funciona", "Les teues dades"],
    "badge": "Fet a l'Horta Sud",
    "h1": "Programari xicotet per a consultes xicotetes.",
    "lead": "Cites per Telegram, factures des del mòbil i fitxes de pacients. Per a fisios, dentistes, psicòlegs i autònoms que volen menys pantalles i més temps amb la gent.",
    "cta1": "Vull provar-ho", "cta2": "Vore les eines",
    "tools_h": "Tres peces, un mateix sòl.",
    "tools_p": "Com les rajoles d'una cuina: cadascuna fa la seua faena i totes encaixen.",
    "live": "En marxa", "pilot": "Pilot",
    "tools": [
      ("Cites per Telegram", "Els pacients trien dia i hora amb botons. Cada negoci té el seu bot i tot cau al teu Google Calendar."),
      ("Factures des del xat", "Un bot per a autònoms: fas la factura des del mòbil, entre un pacient i el següent."),
      ("Gestió de consulta", "Agenda, fitxes de pacients, consentiments signats en tauleta i facturació Verifactu. El just i necessari."),
    ],
    "steps_h": "Com es posa en marxa",
    "steps": [
      ("Ens envies els horaris", "Serveis, durades i dies que treballes."),
      ("Creem el teu bot", "Amb el nom del teu negoci i connectat al teu calendari."),
      ("Compartixes l'enllaç", "I les cites comencen a arribar soles."),
    ],
    "data_h": "Les teues dades, a prop de casa.",
    "data_p": [
      "Treballem com a encarregats del tractament: les dades dels teus pacients són teues i només les usem per a donar-te el servei.",
      "L'agenda viu al nostre servidor i també a l'ordinador de la consulta. Si alguna cosa falla, continues veient les cites.",
    ],
    "contact_h": "Ho provem a la teua consulta?",
    "contact_p": "Estem en fase pilot amb poques consultes. Conta'ns què fas i et direm amb sinceritat si t'encaixa.",
    "tg": "Escriure per Telegram",
    "legal": "Avís legal i privacitat",
    "legal_title": "Avís legal i privacitat",
    "home": "Tornar a l'inici",
  },
  "es": {
    "lang": "es-ES", "prefix": "../", "other": "../",
    "title": "Baulat · Software pequeño para consultas pequeñas",
    "desc": "Citas por Telegram, facturas desde el móvil y gestión de consulta para fisios, dentistas, psicólogos y autónomos. Hecho en la Horta Sud.",
    "skip": "Ir al contenido",
    "nav": ["Herramientas", "Cómo funciona", "Tus datos"],
    "badge": "Hecho en la Horta Sud",
    "h1": "Software pequeño para consultas pequeñas.",
    "lead": "Citas por Telegram, facturas desde el móvil y fichas de pacientes. Para fisios, dentistas, psicólogos y autónomos que quieren menos pantallas y más tiempo con la gente.",
    "cta1": "Quiero probarlo", "cta2": "Ver las herramientas",
    "tools_h": "Tres piezas, un mismo suelo.",
    "tools_p": "Como las baldosas de una cocina: cada una hace su trabajo y todas encajan.",
    "live": "En marcha", "pilot": "Piloto",
    "tools": [
      ("Citas por Telegram", "Tus pacientes eligen día y hora con botones. Cada negocio tiene su propio bot y todo cae en tu Google Calendar."),
      ("Facturas desde el chat", "Un bot para autónomos: haces la factura desde el móvil, entre un paciente y el siguiente."),
      ("Gestión de consulta", "Agenda, fichas de pacientes, consentimientos firmados en tableta y facturación Verifactu. Lo justo y necesario."),
    ],
    "steps_h": "Así se pone en marcha",
    "steps": [
      ("Nos mandas tus horarios", "Servicios, duraciones y días que trabajas."),
      ("Creamos tu bot", "Con el nombre de tu negocio y conectado a tu calendario."),
      ("Compartes el enlace", "Y las citas empiezan a llegar solas."),
    ],
    "data_h": "Tus datos, cerca de casa.",
    "data_p": [
      "Trabajamos como encargados del tratamiento: los datos de tus pacientes son tuyos y solo los usamos para darte el servicio.",
      "La agenda vive en nuestro servidor y también en el ordenador de tu consulta. Si algo falla, sigues viendo tus citas.",
    ],
    "contact_h": "¿Lo probamos en tu consulta?",
    "contact_p": "Estamos en fase piloto con pocas consultas. Cuéntanos qué haces y te diremos con sinceridad si te encaja.",
    "tg": "Escribir por Telegram",
    "legal": "Aviso legal y privacidad",
    "legal_title": "Aviso legal y privacidad",
    "home": "Volver al inicio",
  },
}

LEGAL = {
  "va": """
<h2>Titular</h2>
<p>Titular: Alejandro Ibáñez Colomina · NIF: 53894776A · Adreça: C/Mestre Salvoret, 1 · Correu: <a href="mailto:{email}">{email}</a></p>
<h2>Ús d'aquesta web</h2>
<p>Esta web és informativa. No fa servir galetes de seguiment ni analítica, i les fonts tipogràfiques s'allotgen al mateix servidor.</p>
<h2>Dades personals</h2>
<p>Si ens escrius per correu o Telegram, usarem les teues dades només per a respondre't. Responsable: Alejandro Ibáñez Colomina. Base legal: el teu consentiment en contactar-nos. No les cedim a ningú. Pots exercir els teus drets d'accés, rectificació i supressió escrivint a <a href="mailto:{email}">{email}</a>, i reclamar davant l'Agència Espanyola de Protecció de Dades (aepd.es).</p>
<h2>Dades dels pacients dels nostres clients</h2>
<p>En els serveis de cites, facturació i gestió actuem com a encarregats del tractament, per compte de cada consulta i amb el contracte corresponent.</p>
""",
  "es": """
<h2>Titular</h2>
<p>Titular: Alejandro Ibáñez Colomina · NIF: 53894776A · Adreça: C/Mestre Salvoret, 1 · Correo: <a href="mailto:{email}">{email}</a></p>
<h2>Uso de esta web</h2>
<p>Esta web es informativa. No usa cookies de seguimiento ni analítica, y las fuentes tipográficas se alojan en el mismo servidor.</p>
<h2>Datos personales</h2>
<p>Si nos escribes por correo o Telegram, usaremos tus datos solo para responderte. Responsable: Alejandro Ibáñez Colomina. Base legal: tu consentimiento al contactarnos. No los cedemos a nadie. Puedes ejercer tus derechos de acceso, rectificación y supresión escribiendo a <a href="mailto:{email}">{email}</a>, y reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
<h2>Datos de los pacientes de nuestros clientes</h2>
<p>En los servicios de citas, facturación y gestión actuamos como encargados del tratamiento, por cuenta de cada consulta y con el contrato correspondiente.</p>
""",
}


def head(t, title, desc, path, lang_key):
    p = t["prefix"]
    alt_va = f"{DOMAIN}/{path}"
    alt_es = f"{DOMAIN}/es/{path}"
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#2A4652">
<link rel="alternate" hreflang="ca-ES" href="{alt_va}">
<link rel="alternate" hreflang="es-ES" href="{alt_es}">
<link rel="icon" type="image/png" href="{p}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta property="og:type" content="website">
<link rel="preload" href="{p}assets/fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""


def header(t, lang_key, on_home=True, legal=False):
    p = t["prefix"]
    home = "./"
    anchor = "" if on_home else "./"
    va_href = ("" if lang_key == "va" else "../") + ("legal.html" if legal else "./")
    es_href = ("es/" if lang_key == "va" else "") + ("legal.html" if legal else "./")
    va_cur = 'aria-current="true"' if lang_key == "va" else ""
    es_cur = 'aria-current="true"' if lang_key == "es" else ""
    links = "".join(
        f'<a class="nav-link" href="{anchor}#{i}">{n}</a>'
        for i, n in zip(["eines", "com", "dades"], t["nav"])
    )
    return f"""<header class="site-header">
<div class="wrap">
<a class="logo" href="{home}"><img src="{p}assets/img/baulat-logo.png" alt="Baulat" width="166" height="46"></a>
<nav class="nav" aria-label="Principal">{links}
<span class="lang"><a href="{va_href}" lang="ca" {va_cur}>VAL</a><a href="{es_href}" lang="es" {es_cur}>CAS</a></span>
</nav>
</div>
</header>
"""


def footer(t):
    p = t["prefix"]
    return f"""<div class="strip" aria-hidden="true"></div>
<footer class="site-footer">
<div class="wrap">
<img src="{p}assets/img/baulat-logo.png" alt="Baulat" width="94" height="26">
<span>{t['badge']}</span>
<nav aria-label="Legal"><a href="legal.html">{t['legal']}</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div>
</footer>
</body>
</html>
"""


def home(lang_key):
    t = T[lang_key]
    tiles_cls = ["t1", "t2", "t1", "t2", "t3", "t2", "t1", "t2"]
    tiles = "".join(f'<span class="{c}"></span>' for c in tiles_cls) + '<span class="empty"></span>'
    tool_tiles = ["t1", "t2", "t3"]
    tools = ""
    for i, (h, d) in enumerate(t["tools"]):
        pill = f'<span class="pill pill-yellow">{t["pilot"]}</span>' if i == 2 else f'<span class="pill">{t["live"]}</span>'
        tools += f"""<article class="tool"><div class="tile-band {tool_tiles[i]}" aria-hidden="true"></div>
<div class="tool-body">{pill}<h3>{h}</h3><p>{d}</p></div></article>
"""
    steps = "".join(
        f'<li><p class="num">{n}</p><h3>{h}</h3><p>{d}</p></li>'
        for n, (h, d) in enumerate(t["steps"], 1)
    )
    data_p = "".join(f"<p>{x}</p>" for x in t["data_p"])
    return head(t, t["title"], t["desc"], "", lang_key) + header(t, lang_key) + f"""<main id="main">
<section class="hero">
<div class="wrap">
<div class="hero-text">
<span class="pill pill-yellow">{t['badge']}</span>
<h1>{t['h1']}</h1>
<p class="lead">{t['lead']}</p>
<div class="btns"><a class="btn btn-solid" href="#contacte">{t['cta1']}</a><a class="btn btn-line" href="#eines">{t['cta2']}</a></div>
</div>
<div class="tiles" aria-hidden="true">{tiles}</div>
</div>
</section>
<div class="strip" aria-hidden="true"></div>
<section id="eines" class="section">
<div class="wrap">
<h2 class="accent">{t['tools_h']}</h2>
<p class="section-intro">{t['tools_p']}</p>
<div class="tools">
{tools}</div>
</div>
</section>
<section id="com" class="steps">
<div class="wrap">
<h2>{t['steps_h']}</h2>
<ol>{steps}</ol>
</div>
</section>
<section id="dades" class="section data">
<div class="wrap">
<div class="t2" aria-hidden="true"></div>
<div class="data-text"><h2>{t['data_h']}</h2>{data_p}</div>
</div>
</section>
<section id="contacte" class="contact">
<div class="wrap">
<div class="contact-box">
<div><h2>{t['contact_h']}</h2><p>{t['contact_p']}</p></div>
<div class="contact-actions"><a class="btn btn-solid" href="mailto:{EMAIL}">{EMAIL}</a><a class="btn btn-line" href="{TELEGRAM}" rel="noopener">{t['tg']}</a></div>
</div>
</div>
</section>
</main>
""" + footer(t)


def legal(lang_key):
    t = T[lang_key]
    body = LEGAL[lang_key].format(email=EMAIL)
    return head(t, f"{t['legal_title']} · Baulat", t["desc"], "legal.html", lang_key) + header(t, lang_key, on_home=False, legal=True) + f"""<main id="main" class="legal">
<h1>{t['legal_title']}</h1>
{body}
<p><a href="./">{t['home']}</a></p>
</main>
""" + footer(t)


def write(path, s):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(s)


write("index.html", home("va"))
write("es/index.html", home("es"))
write("legal.html", legal("va"))
write("es/legal.html", legal("es"))
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>{DOMAIN}/</loc></url>
<url><loc>{DOMAIN}/es/</loc></url>
</urlset>
""")
print("ok ->", OUT)
