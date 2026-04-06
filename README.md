# chumbo.io — Web corporativa

Web corporativa de **chumbo.io**, empresa detrás de [SILOE Generator](https://siloegenerator.chumbo.io).

Construida con **Astro** (SSG) → desplegada en **Cloudflare Pages**.

---

## Desarrollo local

```bash
npm install
npm run dev        # http://localhost:4321
```

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
│   ├── SocialProof.astro
│   ├── PricingCards.astro     # reutilizado en / y /precios
│   ├── About.astro
│   ├── Contact.astro
│   └── Footer.astro
├── pages/
│   ├── index.astro            # Home
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
