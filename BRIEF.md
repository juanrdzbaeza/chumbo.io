# BRIEF — Web corporativa chumbo.io

> 📋 Este fichero es el **contexto completo** para construir la web corporativa de chumbo.io.
> Dáselo al agente/copilot que vaya a implementar el proyecto desde cero.

---

## 1. La empresa

| Campo | Valor |
|---|---|
| **Nombre** | chumbo.io |
| **Tipo** | Software startup española — indie/bootstrapped |
| **Fundador** | Juan (solo founder) |
| **Email principal** | soporte@chumbo.io |
| **Dominio** | chumbo.io (registrado en Cloudflare) |
| **Personalidad de marca** | Directa, un pelín gamberra, sin florituras corporativas. Cercana, honesta, técnica pero accesible. Anti-marketing de humo. |
| **Tagline candidato** | *"Software que funciona. Sin humo."* / *"Herramientas serias para gente seria"* / o algo mejor si se te ocurre — manteniendo el tono. |

### Tono de escritura

- **SÍ:** directo, técnico-accesible, con algo de humor seco, confianza sin prepotencia
- **NO:** "soluciones disruptivas", "empoderamos a las empresas", "ecosistema 360", corporativo vacío
- En español por defecto. Inglés opcional en menú/footer.

---

## 2. El producto actual — Siloe-Generator

> El único producto hoy. La web de chumbo.io es su escaparate.

| Campo | Valor |
|---|---|
| **Nombre** | SILOE Generator |
| **Subtítulo** | Libro Digital de Piscinas |
| **URL producción** | https://siloegenerator.chumbo.io |
| **Qué hace** | Sustituye el libro de registro en papel/Excel de una piscina. Gestiona lecturas diarias de parámetros físico-químicos, genera el XML oficial para el sistema SILOE de Sanidad y gestiona muestras de laboratorio. |
| **Marco legal** | Real Decreto 742/2013, de 27 de septiembre — criterios técnico-sanitarios de piscinas |
| **Clientes objetivo** | Hoteles, campings, clubes deportivos, comunidades de vecinos — cualquier establecimiento con piscina de uso público en España |
| **Stack** | Vue 3 + Vite · Node.js/Express · PostgreSQL · Railway · Stripe · Resend |

### Planes de precio (Stripe — modo test activo)

| Plan | Precio | Para quién |
|---|---|---|
| **Starter** | 69 €/mes | 1 establecimiento, hasta 10 piscinas |
| **Pro** | 129 €/mes | Hasta 5 establecimientos |
| **Enterprise** | 299 €/mes | Sin límite de establecimientos |

### Estado del producto (marzo 2026)
- ✅ Registro + confirmación por email (Resend desde `noreply@siloegenerator.chumbo.io`)
- ✅ Pago con Stripe (suscripción mensual)
- ✅ Gestión completa de lecturas diarias y parámetros de laboratorio
- ✅ Generación de XML compatible SILOE
- ✅ Multi-tenant, multi-piscina
- ✅ En producción en Railway
- 🔄 Beta pública (versión `beta-v0.0.4-20260324`)

---

## 3. Infraestructura DNS (Cloudflare)

```
chumbo.io                      →  web corporativa (este proyecto)
siloegenerator.chumbo.io       →  app frontend (Railway)
api.chumbo.io                  →  backend API (Railway)
noreply@siloegenerator.chumbo.io → emails transaccionales (Resend/SES)
soporte@chumbo.io              →  redirige a email personal del fundador
```

---

## 4. Identidad visual

### Concepto de logo — El chumbo con bocadito 🌵

> Inspiración directa del logo de Apple: una fruta icónica con un pequeño mordisco en la parte superior derecha.

**El higo chumbo** (*Opuntia ficus-indica*) es el fruto de la chumbera, planta típica del sur de España y Canarias. Oval, cubierto de pequeñas espinas, con piel gruesa y pulpa interior dulce y jugosa. La metáfora de marca es perfecta:

- 🌵 **Por fuera:** espinoso, directo, no apto para manazas → marca gamberra, sin humo
- 🍊 **Por dentro:** dulce, jugoso, valioso → software que realmente funciona
- 🍎 **El mordisco:** homenaje consciente al logo de Apple, pero con identidad 100% española/canaria

**Por qué funciona:**
- Único en el mundo tech — nadie tiene un higo chumbo como logo
- Auténtico — conecta con las raíces geográficas (Canarias / sur de España)
- Visual — silueta inconfundible, funciona a cualquier tamaño
- Gambero sin esfuerzo — la idea de morderle a un chumbo con espinas ya lo dice todo

### Assets de logo creados

```
public/
├── icon.svg    ← Solo el fruto (200×270 viewBox) — favicon, app icon, redes
└── logo.svg    ← Horizontal: icono + wordmark "chumbo.io" (700×270 viewBox)
```

**Lógica del SVG:**
1. Se dibuja la piel del fruto (`#9B1D35`) con una `<mask>` que recorta el mordisco → **hueco transparente limpio, igual que el logo de Apple** — muestra el fondo a través del recorte
2. Las aréolas (puntos de espinas) siguen el patrón diagonal natural de la *Opuntia*, recortadas al contorno del fruto y enmascaradas en la zona del mordisco
3. La corona superior (sépalos secos) da el detalle botánico característico

### Paleta

| Token | Hex | Rol |
|---|---|---|
| `--chumbo-skin` | `#9B1D35` | Piel del fruto · "chumbo" en wordmark · color principal de marca |
| `--chumbo-flesh` | `#F4A523` | Pulpa interior · ".io" en wordmark · accent/CTA |
| `--chumbo-dark` | `#6E1225` | Corona · versión oscura para hover / sombras |
| `--chumbo-spine` | `#7A1528` | Aréolas · detalles sutiles |
| `--bg-dark` | `#111111` | Fondos oscuros (hero, secciones de impacto) |
| `--bg-light` | `#FAFAF8` | Fondos claros (secciones de contenido) |

> 💡 El `.io` del wordmark usa `#F4A523` (la pulpa) — crea coherencia visual entre el mordisco del icono y el texto. Es el detalle de diseño que lo une todo.

### Tipografía

| Rol | Fuente | Instalación |
|---|---|---|
| Wordmark / Títulos | **Space Grotesk** | `npm i @fontsource/space-grotesk` |
| Cuerpo / UI | **Inter** | `npm i @fontsource/inter` |

- Self-hosted via Fontsource (sin Google Fonts → privacidad)
- Fallback stack: `'Space Grotesk', 'Plus Jakarta Sans', Inter, system-ui, sans-serif`

### Assets de Siloe-Generator (referencia)

```
Siloe-Generator/frontend/public/icons/icon.svg   ← gota de agua (icono SILOE)
Siloe-Generator/frontend/public/icons/logo.svg   ← logo horizontal SILOE 512×192
```

---

## 5. Stack recomendado para la web corporativa

### Opción A — **Astro** (recomendado ⭐)

```bash
npm create astro@latest chumbo.io -- --template minimal
# + integración Vue si se quieren componentes interactivos
```

- SSG puro → HTML estático → despliegue en Cloudflare Pages (gratis, ya tenemos CF)
- Velocidad máxima, SEO perfecto
- Puede usar componentes Vue (que ya conocemos del proyecto)
- Zero JS por defecto salvo donde se necesite

### Opción B — HTML/CSS vanilla + Tailwind

- Máximo control, cero dependencias de framework
- Ideal si la web es básica (landing page)

### Despliegue

**Cloudflare Pages** es la opción natural (dominio ya en Cloudflare):
```
# Build command:  npm run build
# Output dir:     dist/
# Branch:         main
```
O Railway si se prefiere consistencia con el resto del stack.

---

## 6. Estructura de la web (mínimo viable)

### Páginas

```
/                   → Home / Landing page principal
/productos          → Detalle de Siloe-Generator (o sección en home)
/precios            → Planes y precios
/legal              → Aviso legal + política de privacidad + cookies
/contacto           → Formulario o mailto directo
```

### Secciones del Home (propuesta)

1. **Hero** — Tagline impactante + CTA → "Ver Siloe-Generator"
2. **El problema** — Por qué existe chumbo.io (el libro de piscinas en Excel es un caos)
3. **La solución** — Siloe-Generator en 3 bullets/cards
4. **Prueba social** — "*Beta en producción · Primeros clientes · Cumple RD 742/2013*"
5. **Precios** — Las 3 cards de planes
6. **Sobre chumbo.io** — 2-3 líneas honestas sobre el fundador y la misión
7. **Contacto** — `soporte@chumbo.io` + link a la app
8. **Footer** — © chumbo.io · Aviso legal · `soporte@chumbo.io`

---

## 7. Requisitos técnicos clave

- [ ] **Performance:** Lighthouse ≥ 90 en todas las métricas
- [ ] **SEO básico:** meta title/description, og:tags, sitemap.xml, robots.txt
- [ ] **Sin cookies de terceros** en primera carga (no Google Analytics por defecto)
- [ ] **Responsive** — mobile-first
- [ ] **HTTPS** — vía Cloudflare automático
- [ ] **Sin formulario de contacto complejo** — `mailto:soporte@chumbo.io` es suficiente para MVP
- [ ] **CTA principal** → `https://siloegenerator.chumbo.io` (registro/login)

---

## 8. Lo que NO hacer

- ❌ Stock photos genéricas de gente sonriendo con ordenadores
- ❌ Frases vacías tipo "Transformamos tu negocio"
- ❌ Animaciones pesadas que ralenticen la carga
- ❌ Cookie banners agresivos (si no hay tracking, no hay banner)
- ❌ Dark patterns en los CTAs
- ❌ Fingir que somos 50 empleados cuando somos 1

---

## 9. Contexto adicional

### Sobre el RD 742/2013

El Real Decreto 742/2013 obliga a los titulares de piscinas de uso público a llevar un **libro de registro** de los parámetros físico-químicos del agua (cloro, pH, temperatura, turbiedad...) y a declarar los datos al sistema SILOE del Ministerio de Sanidad mediante un XML en formato específico. Siloe-Generator automatiza exactamente eso.

### Por qué "chumbo"

> El nombre es una referencia directa, sin filtros — como el plomo (chumbo en portugués/argot) que va al grano. Software que hace lo que dice, sin adornos.

### Estado actual del negocio

- Fundador técnico solo, sin inversión externa
- Producto en beta pública con primeros clientes reales
- Ingresos recurrentes vía Stripe (modelo SaaS mensual)
- Próximos pasos: crecer base de clientes → ampliar producto

---

## 10. Entregables esperados del agente

1. **Inicializar proyecto** Astro (o el stack elegido) en `/home/juan/Documentos/IdeaProjects/chumbo.io`
2. **Crear estructura de ficheros** completa
3. **Implementar todas las secciones** del Home descritas en §6
4. **Implementar `/precios`** con las 3 cards (Starter/Pro/Enterprise)
5. **Implementar `/legal`** con aviso legal básico para España (adaptable)
6. **Footer** con © chumbo.io, enlaces legales, `soporte@chumbo.io`
7. **README.md** del proyecto con instrucciones de desarrollo y despliegue
8. **`package.json`** con scripts `dev`, `build`, `preview`

---

*Brief generado el 24 marzo 2026 · chumbo.io · soporte@chumbo.io*

