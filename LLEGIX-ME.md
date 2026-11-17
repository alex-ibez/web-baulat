# Web de Baulat

Web estàtica (HTML + CSS, sense JavaScript ni galetes). Valencià a `/`, castellà a `/es/`.

## Abans de publicar
Obri `build.py`, canvia aquestes tres línies i executa `python3 build.py .`:
- `DOMAIN` → el teu domini (p. ex. `https://baulat.es`)
- `EMAIL` → correu de contacte
- `TELEGRAM` → enllaç `https://t.me/...`

Després omple les dades del titular ([NOM], [NIF], [ADREÇA]) dins de `build.py` (bloc `LEGAL`) i torna a executar-lo.
Tots els textos de la web estan al diccionari `T` del mateix fitxer.

## Publicar a Netlify
1. app.netlify.com → Add new site → Deploy manually → arrossega aquesta carpeta.
2. Domain management → Add a domain → el teu domini.

## Connectar el domini de Squarespace Domains
Squarespace → Domains → el domini → DNS → DNS Settings:
1. Esborra els registres de "Squarespace Defaults" (A i CNAME www).
2. A "Custom Records" afig:
   - `@`   A      `75.2.60.5`
   - `www` CNAME  `<nom-del-site>.netlify.app`
3. Espera la propagació (minuts o unes hores). Netlify activa l'HTTPS sol.

No toques els registres MX si tens correu en eixe domini.

## Logo
`assets/img/baulat-logo.png` està retallat de la imatge. Quan tingues el logo en SVG, substitueix-lo
i canvia l'extensió a `build.py`.
