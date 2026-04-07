"""
Convierte los SVG de public/ a PNG y JPG para registro OEPM.
Usa Playwright + Chromium headless para un renderizado fiel al navegador
(masks, clip-paths, fuentes incluidas).

Uso:
    python scripts/convert-logos.py

Requisitos (una sola vez):
    pip install playwright pillow
    python -m playwright install chromium
"""

import asyncio
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright

PUBLIC = Path(__file__).parent.parent / "public"
OUT    = PUBLIC / "oepm"
OUT.mkdir(exist_ok=True)

# Dimensiones de render (píxeles) para cada SVG según su viewBox
SIZES = {
    "icon.svg":            (800, 1080),
    "favicon.svg":         (800, 1080),
    "logo.svg":            (2000,  771),
    "logo-chumbosoft.svg": (2000,  771),
}


async def convert():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for svg_path in sorted(PUBLIC.glob("*.svg")):
            w, h = SIZES.get(svg_path.name, (2000, 800))

            # Envolvemos el SVG en HTML para forzar dimensiones exactas
            html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{w}px; height:{h}px; overflow:hidden; background:transparent; }}
  img {{ width:{w}px; height:{h}px; display:block; }}
</style>
</head>
<body>
<img src="file:///{svg_path.as_posix()}"/>
</body>
</html>"""

            html_file = OUT / f"_tmp_{svg_path.stem}.html"
            html_file.write_text(html, encoding="utf-8")

            page = await browser.new_page(viewport={"width": w, "height": h})
            await page.goto(f"file:///{html_file.as_posix()}")
            await page.wait_for_timeout(300)   # espera a que cargue el SVG

            png_path = OUT / f"{svg_path.stem}.png"
            await page.screenshot(path=str(png_path), full_page=False, omit_background=True)
            await page.close()
            html_file.unlink()

            # PNG → JPG con fondo blanco (OEPM no siempre acepta transparencia)
            jpg_path = OUT / f"{svg_path.stem}.jpg"
            with Image.open(png_path).convert("RGBA") as im:
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[3])
                bg.save(jpg_path, format="JPEG", quality=95)

            size_info = Image.open(png_path).size
            print(f"✓  {svg_path.name}  →  {png_path.name} {size_info}  |  {jpg_path.name}")

        await browser.close()
        print(f"\nArchivos en: {OUT}")


if __name__ == "__main__":
    asyncio.run(convert())

