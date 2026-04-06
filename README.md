# chumbo.io — Web corporativa

Web corporativa de **chumbo.io**, empresa detrás de [SILOE Generator](https://siloegenerator.chumbo.io).

Incluye también la presentación de **DNIBridge** como proyecto en desarrollo activo.

Construida con **Astro** (SSG) → desplegada en **Cloudflare Pages**.

---

## Prerequisito: Node ≥ 18

El proyecto usa **Astro 6** que requiere Node ≥ 18. El sistema puede tener Node 12 como versión por defecto.
Usamos **nvm** para gestionar la versión correcta:

```bash
# Primera vez: instalar nvm (si no está)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc

# Instalar y usar el Node LTS
nvm install --lts
nvm use --lts          # v24.x actualmente
```

Una vez instalado nvm y Node LTS, al abrir un terminal nuevo se carga automáticamente.

## Desarrollo local

```bash
npm install
npm run dev        # http://localhost:4321
```

> **IntelliJ:** Las run configurations `.run/dev.run.xml` y `.run/build.run.xml` ya están configuradas
> apuntando a `/home/juan/.nvm/versions/node/v24.14.1/bin/node`. Aparecerán en el menú de Run.

## Build y preview

```bash
npm run build      # genera dist/
npm run preview    # sirve dist/ localmente
```

## Estructura

```
src/
├── layouts/Layout.astro       # shell HTML, meta SEO, OG tags
├── components/
│   ├── Nav.astro
│   ├── Hero.astro
│   ├── Problem.astro
│   ├── Solution.astro
│   ├── BetaPublic.astro
│   ├── SocialProof.astro
│   ├── PricingCards.astro     # reutilizado en / y /precios
│   ├── About.astro
│   ├── ActiveProjects.astro
│   ├── Contact.astro
│   └── Footer.astro
├── pages/
│   ├── index.astro            # Home
│   ├── productos.astro         # SILOE Generator + DNIBridge
│   ├── precios.astro          # Planes y precios
│   ├── legal.astro            # Aviso legal / privacidad / cookies
│   └── contacto.astro         # Contacto
└── styles/global.css          # Variables de marca, reset, utilidades

public/
├── icon.svg                   # Favicon / app icon
├── logo.svg                   # Logo horizontal (nav, footer)
├── favicon.svg
├── apple-touch-icon.png       # 180×180
└── robots.txt
```

## Despliegue en Cloudflare Pages

1. Conecta el repo desde el [dashboard de Cloudflare Pages](https://pages.cloudflare.com/)
2. Configura:
   - **Framework preset:** Astro
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
3. Asigna el dominio personalizado `chumbo.io` desde la pestaña *Custom domains*

El sitemap se genera automáticamente en `dist/sitemap-index.xml`.

---

## Brief

Ver [`BRIEF.md`](./BRIEF.md) para el contexto completo del proyecto.

---

*© 2026 chumbo.io · soporte@chumbo.io*
