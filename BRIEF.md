# BRIEF — Web corporativa chumbo.io

> 📋 Este fichero es el **contexto completo** para construir la web corporativa de chumbo.io.
> Dáselo al agente/copilot que vaya a implementar o actualizar el proyecto.
> **Última actualización: 6 abril 2026**

---

## 1. La empresa

| Campo                     | Valor                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Nombre comercial**      | chumbo.io                                                                                                                  |
| **Razón social**          | Chumbosoft, S.L. *(inscrita en el Registro Mercantil Central)*                                                             |
| **Marca registrada**      | Logo-chumbosoft registrado en la Oficina Española de Patentes y Marcas (OEPM) — en trámite de concesión                    |
| **Tipo**                  | Software startup española — indie/bootstrapped                                                                             |
| **Fundador**              | Juan (solo founder)                                                                                                        |
| **Email soporte**         | soporte@chumbo.io (redirige a email personal del fundador)                                                                 |
| **Dominio**               | chumbo.io (registrado en Cloudflare)                                                                                       |
| **Proyectos activos**     | SILOE Generator + DNIBridge                                                                                                |
| **Personalidad de marca** | Directa, un pelín gamberra, sin florituras corporativas. Cercana, honesta, técnica pero accesible. Anti-marketing de humo. |
| **Tagline candidato**     | *"Software que funciona. Sin humo."*                                                                                       |

### Tono de escritura

- **SÍ:** directo, técnico-accesible, con algo de humor seco, confianza sin prepotencia
- **NO:** "soluciones disruptivas", "empoderamos a las empresas", "ecosistema 360", corporativo vacío
- En español por defecto. Inglés opcional en menú/footer.

---

## 2. Productos actuales

> chumbo.io ya tiene producto en producción (SILOE Generator) y también desarrolla DNIBridge.

### 2.1 SILOE Generator (producto principal actual)

| Campo                 | Valor                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nombre**            | SILOE Generator                                                                                                                                                                                                   |
| **Subtítulo**         | Libro Digital de Piscinas                                                                                                                                                                                         |
| **URL producción**    | https://siloegenerator.chumbo.io                                                                                                                                                                                  |
| **URL API**           | https://api.chumbo.io                                                                                                                                                                                             |
| **Versión actual**    | `beta-v0.0.9-20260505`                                                                                                                                                                                            |
| **Qué hace**          | Sustituye el libro de registro en papel/Excel de una piscina. Gestiona lecturas diarias de parámetros físico-químicos, genera el XML oficial para el sistema SILOE de Sanidad y gestiona muestras de laboratorio. |
| **Marco legal**       | Real Decreto 742/2013, de 27 de septiembre — criterios técnico-sanitarios de piscinas                                                                                                                             |
| **Clientes objetivo** | Hoteles, campings, clubes deportivos, comunidades de vecinos — cualquier establecimiento con piscina de uso público en España                                                                                     |
| **Stack**             | Vue 3 + Vite · Node.js/Express · PostgreSQL · Railway · Stripe · Resend                                                                                                                                           |

### Planes de precio ✅ confirmados en Stripe

| Plan                 | Precio     | Límites                       | Para quién                                            |
|----------------------|------------|-------------------------------|-------------------------------------------------------|
| 🌵 **Beta gratuita** | **Gratis** | 1 establecimiento · 1 piscina | Acceso público temporal durante la beta — sin tarjeta |
| **Starter**          | 69 €/mes   | Hasta 4 piscinas              | Pequeño establecimiento individual                    |
| **Pro**              | 129 €/mes  | Hasta 9 piscinas              | Establecimiento mediano o varios hoteles              |
| **Enterprise**       | 299 €/mes  | Hasta 20 piscinas             | Cadenas hoteleras, empresas de mantenimiento          |
| **Platinum**         | -          | -                             | Contactar con soporte@chumbo.io para el caso          |

> **Importante sobre la Beta gratuita:** Es temporal durante la beta pública. El usuario puede hacer upgrade a cualquier plan de pago sin perder sus datos (flujo transparente vía Stripe).

### 🧠 Pricing v2 — en estudio (no implementado aún)

> **Contexto:** El modelo de pricing v1 (límite por piscinas totales) tiene una vulnerabilidad: una empresa de mantenimiento puede meter todas las piscinas de 50 hoteles bajo un solo establecimiento y pagar el plan más barato. El modelo v2 busca cerrar ese gap y ser más justo con el volumen real.

#### El problema del agregador

Una empresa de mantenimiento que lleva 50 hoteles × 2 piscinas cada uno podría:
1. Darse de alta con 1 establecimiento ficticio ("Gestión Piscinas S.L.")
2. Meter las 100 piscinas ahí
3. Pagar Enterprise → 299€/mes
4. Descargar el XML, retocarlo a mano (texto plano) con el código de establecimiento y código de vaso de cada hotel real
5. Subir manualmente a SILOE por cada hotel
6. **Ahorro: 50 × 69€ = 3.450€ → paga solo 299€** 🚨

**Nota legal:** quien retoca y sube el XML a SILOE asume la responsabilidad legal de ese XML. Si hay error o auditoría, el problema es del usuario, no de Chumbosoft.

#### Modelo v2 propuesto: volume pricing por piscinas (con techo)

Precio por piscina que decrece con el volumen, pero **siempre con un máximo** (no infinito).
El establecimiento más grande estimado en Canarias: ~100 piscinas (hotel de lujo con piscina por habitación).

| Tramo       | Piscinas incluidas | Precio/piscina | Total/mes aprox. | Nombre sugerido |
|-------------|--------------------|----------------|------------------|-----------------|
| 🌵 Beta     | 1                  | Gratis         | Gratis           | Beta            |
| Tramo 1     | 1                  | ~19 €/piscina  | ~19 €            | Solo            |
| Tramo 2     | hasta 5            | ~15 €/piscina  | hasta ~75 €      | Pequeño         |
| Tramo 3     | hasta 25           | ~11 €/piscina  | hasta ~275 €     | Mediano         |
| Tramo 4     | hasta 100          | ~6 €/piscina   | hasta ~600 €     | Grande          |
| ♾️ Platinum | +100               | A medida       | —                | Platinum        |

> ⚠️ Los precios son orientativos — pendiente de validar con primeros usuarios de pago reales.

**Variantes a decidir:**
- **Volume pricing** (todo se cobra al precio del tramo en que caes — más simple de comunicar) vs. **Tiered pricing** (cada tramo a su precio — más justo pero difícil de explicar en la web). **Recomendación: Volume pricing.**
- Añadir un segundo límite de **establecimientos por cuenta** además de piscinas, para dificultar aún más el gaming del agregador.
- Stripe soporta Graduated Pricing de forma nativa — no requiere lógica manual en el backend.

**Pendiente de decisión antes de implementar:** ¿el límite aplica por piscinas totales en la cuenta o por piscinas por establecimiento?

#### 🏆 La joya de la corona — roadmap estratégico

> **Envío directo a SILOE desde SG** (pendiente de investigar si SILOE expone endpoint/API)
>
> `SG → genera XML → lo envía directo al endpoint de SILOE con las credenciales del establecimiento`
>
> Si SG es quien envía, el XML nunca sale en texto plano al usuario → elimina el retoque manual → cierra el gaming definitivamente → y de paso da un valor enorme al cliente legítimo (ya no tiene que subir nada a mano).
>
> **Acción pendiente:** investigar si `hospedajes.ses.mir.es` o el sistema SILOE del Ministerio de Sanidad exponen algún endpoint SOAP/REST para envío programático de XMLs. Preguntar también en la solicitud a la Policía Nacional (ya enviada) si hay documentación técnica de integración disponible.
>
> **Contacto técnico SILOE — Ministerio de Sanidad:** `aguas@sanidad.gob.es`
> Posible canal para consultar soporte técnico de SILOE, documentación de integración y/o endpoint de envío programático de XMLs. Pendiente de contactar.

### Flujo de registro y pago

1. Usuario elige plan en `/precios` y rellena el formulario
2. Recibe email de confirmación desde `noreply@siloegenerator.chumbo.io` (vía Resend)
3. **Si beta:** clic en el enlace → cuenta activada directamente (sin Stripe)
4. **Si plan de pago:** clic en el enlace → redirige a Stripe Checkout → pago → webhook activa la cuenta
5. Usuario ya puede iniciar sesión en `https://siloegenerator.chumbo.io`

### Estado del producto — 30 marzo 2026

- ✅ Registro con confirmación por email (Resend desde `noreply@siloegenerator.chumbo.io`)
- ✅ **Beta pública gratuita** (1 hotel, 1 piscina, sin tarjeta)
- ✅ Upgrade transparente de beta a plan de pago (datos conservados)
- ✅ Pago con Stripe (suscripción mensual, webhooks configurados)
- ✅ Portal de facturación Stripe para usuarios de pago
- ✅ Gestión completa de lecturas diarias y parámetros de laboratorio
- ✅ Análisis de laboratorio
- ✅ Generación de XML compatible SILOE (RD 742/2013)
- ✅ Multi-tenant, multi-hotel, multi-piscina
- ✅ Límites por plan aplicados en backend (piscinas y hoteles)
- ✅ Cron job de limpieza de registros huérfanos
- ✅ Descarga de plantilla XLSX propia de Siloe-Generator
- ✅ PWA instalable (service worker, manifest)
- ✅ En producción en Railway (EU West)
- ✅ Dominios propios vía Cloudflare (`siloegenerator.chumbo.io`, `api.chumbo.io`)
- ✅ Footer con versión, aviso legal, RD 742/2013, contacto
- ✅ Migración `20260330_add_force_password_change.sql` añadida (campo `force_password_change` en users)
- ✅ Forzar cambio de contraseña (feature ready, pendiente de pruebas e2e)
- 🔄 Pendiente: feedback de primeros usuarios beta reales

### 2.2 DNIBridge (nuevo proyecto activo)

| Campo                   | Valor                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nombre**              | DNIBridge                                                                                                                                                                                                                                                                                                                                                                                      |
| **Subtítulo**           | Verificación del QR dinámico de MiDNI                                                                                                                                                                                                                                                                                                                                                          |
| **Repositorio**         | Proyecto separado (`DNIBridge`)                                                                                                                                                                                                                                                                                                                                                                |
| **URL pre-release**     | https://dnibridge-pre.chumbo.io                                                                                                                                                                                                                                                                                                                                                                |
| **Qué hace**            | Webapp que escanea, parsea y verifica criptográficamente el QR del DNI digital español (MiDNI), sin hardware adicional.                                                                                                                                                                                                                                                                        |
| **Marco legal**         | Real Decreto 255/2025 (aceptación obligatoria del DNI digital desde 2026-04-02)                                                                                                                                                                                                                                                                                                                |
| **Stack**               | Vue 3 + Vite + `qr-scanner` + `jsQR` + `@zxing/library`                                                                                                                                                                                                                                                                                                                                        |
| **Estado (abril 2026)** | ✅ Validado con DNI real (miDNI del fundador). Decodificación robusta en cascada, validación ECDSA P-256 operativa, pruebas activas en iOS. Contacto iniciado con la Dirección General de la Policía Nacional (petición vía sede electrónica). Foco geográfico inicial: **Canarias como laboratorio turístico**. Siguientes pasos: integración con SES Hospedajes y evolución hacia mercado UE. |

Notas para la web corporativa:
- Mostrar DNIBridge como **proyecto en desarrollo activo** de chumbo.io.
- No mezclar pricing de SILOE con DNIBridge (DNIBridge no tiene planes comerciales públicos definidos todavía).
- Mantener CTA principal de negocio en SILOE Generator, pero mencionar DNIBridge en `/productos` y en Home.
- Mencionar el **foco inicial en Canarias** como laboratorio turístico — mercado UE como horizonte, no como promesa hoy.
- Mencionar que funciona con **DNI real** (validación criptográfica operativa).

---

## 3. Infraestructura DNS (Cloudflare) ✅ confirmada y funcionando

```
chumbo.io                          →  web corporativa (este proyecto)
siloegenerator.chumbo.io           →  app frontend (Railway · CNAME)
api.chumbo.io                      →  backend API (Railway · CNAME)
dnibridge-pre.chumbo.io            →  DNIBridge pre-release (Cloudflare Workers)
noreply@siloegenerator.chumbo.io   →  emails transaccionales (Resend · SPF+DKIM verificados)
soporte@chumbo.io                  →  redirige a email personal del fundador (Cloudflare Email Routing)
```

### Variables de entorno importantes (no incluir secretos aquí — documentar claves en Railway)

- `DATABASE_URL` — URL de la BD PostgreSQL (Railway/Postgres)
- `NODE_ENV` — `production` en despliegue
- `JWT_SECRET`, `JWT_EXPIRES` — tokens y expiración
- `CORS_ORIGINS`, `FRONTEND_URL` — dominios permitidos (`https://siloegenerator.chumbo.io`)
- `STRIPE_*` — claves y precios en Stripe
- `RESEND_API_KEY` — clave de Resend (guardar en Railway secrets)
- `EMAIL_FROM` — remitente para emails transaccionales (`SILOE Generator <noreply@siloegenerator.chumbo.io>`)

Nota: No incluir valores secretos directamente en este BRIEF. Guardar en el gestor de variables del entorno del proveedor (Railway / Cloudflare Pages / Netlify según corresponda).

---

## 4. Identidad visual

### Concepto de logo — El chumbo con bocadito 🌵

> Inspiración directa del logo de Apple: una fruta icónica con un pequeño mordisco en la parte superior derecha.

**El higo chumbo** (*Opuntia ficus-indica*) es el fruto de la chumbera, planta típica del sur de España y Canarias. Oval, cubierto de pequeñas espinas, con piel gruesa y pulpa interior dulce y jugosa. La metáfora de marca es perfecta:

- 🌵 **Por fuera:** espinoso, directo, no apto para manazas → marca gamberra, sin humo
- 🍊 **Por dentro:** dulce, jugoso, valioso → software que realmente funciona
- 🍎 **El mordisco:** homenaje consciente al logo de Apple, pero con identidad 100% española/canaria

### Assets de logo — ⚠️ ya existen en `public/`, NO recrear

```
public/
├── icon.svg    ← Solo el fruto (200×270 viewBox) — favicon, app icon, redes sociales
└── logo.svg    ← Horizontal: icono + wordmark "chumbo.io" (700×270 viewBox)
```

**Estado final del icono:**
- Forma: trapecio redondeado — top casi plano y ancho, bottom ligeramente más estrecho
- Mordisco: hueco transparente circular en la parte superior derecha (continuidad C1 perfecta)
- **13 aréolas** en patrón diagonal (número con significado personal para el fundador)
- Tallito + hojita separados del fruto por un gap de 8px, estilo Apple
- Color único: `#9B1D35` (variante colorada/madura)

### Paleta

| Token            | Hex       | Rol                                                     |
|------------------|-----------|---------------------------------------------------------|
| `--chumbo-skin`  | `#9B1D35` | Piel del fruto · "chumbo" en wordmark · color principal |
| `--chumbo-flesh` | `#F4A523` | Pulpa · ".io" en wordmark · accent/CTA                  |
| `--chumbo-dark`  | `#6E1225` | Corona · hover / sombras                                |
| `--chumbo-spine` | `#7A1528` | Aréolas · detalles sutiles                              |
| `--bg-dark`      | `#111111` | Fondos oscuros (hero, secciones de impacto)             |
| `--bg-light`     | `#FAFAF8` | Fondos claros (secciones de contenido)                  |

> 💡 El `.io` del wordmark usa `#F4A523` — crea coherencia visual con el mordisco del icono.

### Tipografía

| Rol                | Fuente            | Instalación                       |
|--------------------|-------------------|-----------------------------------|
| Wordmark / Títulos | **Space Grotesk** | `npm i @fontsource/space-grotesk` |
| Cuerpo / UI        | **Inter**         | `npm i @fontsource/inter`         |

- Self-hosted via Fontsource (sin Google Fonts → privacidad)

---

## 5. Stack recomendado para la web corporativa

### **Astro** ⭐ (recomendado)

```bash
npm create astro@latest chumbo.io -- --template minimal
```

- SSG puro → HTML estático → Cloudflare Pages (gratis, dominio ya en CF)
- Velocidad máxima, SEO perfecto, zero JS por defecto
- Puede usar componentes Vue donde se necesite interactividad

### Despliegue — Cloudflare Pages

```
Build command:  npm run build
Output dir:     dist/
Branch:         main
Custom domain:  chumbo.io
```

---

## 6. Estructura de la web

### Páginas

```
/           →  Home / Landing page principal
/productos  →  Detalle de productos: SILOE Generator + DNIBridge
/precios    →  Planes y precios (con CTA → siloegenerator.chumbo.io)
/legal      →  Aviso legal + política de privacidad
/contacto   →  mailto directo soporte@chumbo.io
```

### Secciones del Home

1. **Hero** — Tagline + CTA "Probar gratis" → `https://siloegenerator.chumbo.io/precios`
2. **El problema** — El libro de piscinas en papel/Excel es un caos + riesgo legal
3. **La solución** — Siloe-Generator en 3 bullets concretos
4. **Beta pública gratuita** — *"Pruébalo sin tarjeta. 1 establecimiento, 1 piscina. Cuando te convenza, pasas a un plan."*
5. **Planes y precios** — Las **4 cards en una sola fila**: Beta gratis · Starter 69€ · Pro 129€ · Enterprise 299€
6. **Cumplimiento legal** — RD 742/2013, XML SILOE, trazabilidad
7. **Sobre chumbo.io** — 2-3 líneas honestas sobre el fundador y la misión
8. **Proyectos activos** — mini bloque con SILOE Generator (producción) + DNIBridge (activo en desarrollo)
9. **Contacto** — `soporte@chumbo.io`
10. **Footer** — © chumbo.io · Aviso legal · `soporte@chumbo.io` · versión

### ⚠️ Sobre la sección de precios (4 tarjetas en fila)

Las 4 cards deben caber en **una sola fila** en desktop — en Siloe-Generator ya está resuelto con `col-lg-3`. En la web corporativa aplicar el mismo criterio: 4 columnas en pantallas grandes, 2×2 en tablet, 1 columna en móvil.

---

## 7. Requisitos técnicos

- [ ] **Performance:** Lighthouse ≥ 90
- [ ] **SEO:** meta title/description, og:tags, sitemap.xml, robots.txt
- [ ] **Sin cookies de terceros** en primera carga
- [ ] **Responsive** — mobile-first
- [ ] **HTTPS** — vía Cloudflare automático
- [ ] **CTA principal** → `https://siloegenerator.chumbo.io/precios` (registro/login)
- [ ] **CTA beta** → botón destacado "Probar gratis" → misma URL con `#beta` o directo

---

## 8. Lo que NO hacer

- ❌ Stock photos genéricas de gente sonriendo con ordenadores
- ❌ Frases vacías tipo "Transformamos tu negocio"
- ❌ Animaciones pesadas
- ❌ Cookie banners agresivos (si no hay tracking, no hay banner)
- ❌ Dark patterns en los CTAs
- ❌ Fingir que somos 50 empleados cuando somos 1
- ❌ Decir que el plan beta es permanente — es **temporal durante la beta pública**

---

## 9. Contexto adicional

### Sobre el RD 742/2013

El Real Decreto 742/2013 obliga a los titulares de piscinas de uso público a llevar un **libro de registro** de los parámetros físico-químicos del agua (cloro, pH, temperatura, turbiedad...) y a declarar los datos al sistema SILOE del Ministerio de Sanidad mediante un XML en formato específico. Siloe-Generator automatiza exactamente eso.

### Por qué "chumbo"

> El **higo chumbo** (*Opuntia ficus-indica*) es el fruto de la chumbera — planta típica de Canarias y el sur de España. Por fuera está lleno de espinas y parece difícil de manejar. Por dentro es dulce, jugoso y nutritivo. Es exactamente la metáfora de lo que queremos ser: software que parece directo y sin adornos, pero que por dentro entrega valor real. Además es auténtico, canario, y nadie en el mundo tech tiene un higo chumbo como logo.

### Estado actual del negocio — 7 abril 2026

- Fundador técnico solo, sin inversión externa
- **Chumbosoft, S.L.** inscrita en el Registro Mercantil Central ✅
- **Logo-chumbosoft registrado en la OEPM** (marca en trámite de concesión) ✅
- Producto en **beta pública activa** — versión `beta-v0.0.9-20260505`
- Primeros usuarios reales en producción
- Ingresos recurrentes vía Stripe (modelo SaaS mensual)
- BD de producción limpia: cuentas root (`admin@siloe.com`, `juanrdzbaeza@gmail.com`) + tenant ANCOTUR (pruebas internas)
- Infraestructura: Railway (EU West · Amsterdam) + Cloudflare + Resend + Stripe
- DNIBridge activo como segunda línea de producto (identidad digital / verificación MiDNI)

---

## 10. Entregables esperados del agente

> **Ya existe en el repo** (no tocar):
> - ✅ Git inicializado en `main`
> - ✅ `public/icon.svg` y `public/logo.svg` creados y finalizados
> - ✅ `BRIEF.md` (este fichero) y `README.md`

**Lo que queda por hacer / actualizar:**

1. **Inicializar Astro** dentro del directorio existente sin sobreescribir `public/`, `BRIEF.md`, `README.md`
2. **Integrar** `public/icon.svg` y `public/logo.svg` en la estructura Astro
3. **Favicon:** `favicon.ico` + `favicon.svg` + `apple-touch-icon.png` desde `icon.svg`
4. **Home completo** con todas las secciones de §6, incluyendo la **sección de beta pública** como CTA destacado
5. **`/precios`** con las **4 cards** (Beta gratis · Starter 69€ · Pro 129€ · Enterprise 299€) en una sola fila en desktop, CTA → `https://siloegenerator.chumbo.io/precios`
6. **`/legal`** — aviso legal España (LOPD/RGPD)
7. **Footer** — © 2026 chumbo.io · enlaces legales · `soporte@chumbo.io`
8. **Fuentes** Space Grotesk + Inter vía Fontsource
9. **README.md** actualizado con instrucciones de desarrollo y despliegue en Cloudflare Pages
10. **package.json** con scripts `dev`, `build`, `preview`
11. **Migraciones / DB**: comprobar que `backend/migrations/20260330_add_force_password_change.sql` existe y que `backend/scripts/init-db.js` lo referencia (para que la migración se aplique en despliegues automáticos). Si no está referenciada, añadirla a `init-db.js`.
12. **Tag & Release**: crear tag git `beta/v0.0.9-20260505` y preparar release notes mínimas en el changelog: destacar `force_password_change`, mejoras mobile-first y correcciones de duplicados en lecturas.
13. **Contenido corporativo actualizado**: reflejar explícitamente en Home y `/productos` que chumbo.io también desarrolla **DNIBridge** (sin crear pricing inventado para ese proyecto).

---

*Brief actualizado: 15 abril 2026 · chumbo.io · soporte@chumbo.io*
