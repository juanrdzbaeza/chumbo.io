#!/bin/bash

# Script para exportar el logo CHUMBOSOFT a diferentes formatos
# para enviar a Apple Inc.

LOGO_SVG="/home/juan/Documentos/IdeaProjects/chumbo.io/public/logo-chumbosoft.svg"
OUTPUT_DIR="/home/juan/Documentos/IdeaProjects/chumbo.io/docs/export-apple"

# Crear directorio de salida
mkdir -p "$OUTPUT_DIR"

echo "═══════════════════════════════════════════════"
echo "  Exportando logo CHUMBOSOFT para Apple Inc."
echo "═══════════════════════════════════════════════"
echo ""

# Verificar si existe Inkscape (mejor para conversión SVG)
if command -v inkscape &> /dev/null; then
    echo "✓ Usando Inkscape para conversión de alta calidad..."

    # PNG alta resolución (para email)
    inkscape "$LOGO_SVG" \
        --export-filename="$OUTPUT_DIR/logo-chumbosoft-nuevo.png" \
        --export-width=2000 \
        --export-background=white

    # PDF (vectorial)
    inkscape "$LOGO_SVG" \
        --export-filename="$OUTPUT_DIR/logo-chumbosoft-nuevo.pdf"

    echo "✓ Archivos exportados con Inkscape"

elif command -v convert &> /dev/null; then
    echo "✓ Usando ImageMagick para conversión..."

    # PNG (ImageMagick)
    convert -background white -density 300 "$LOGO_SVG" \
        -resize 2000x "$OUTPUT_DIR/logo-chumbosoft-nuevo.png"

    echo "✓ PNG exportado con ImageMagick"
    echo "⚠ Para PDF, instala Inkscape: sudo apt install inkscape"

elif command -v rsvg-convert &> /dev/null; then
    echo "✓ Usando rsvg-convert para conversión..."

    # PNG (rsvg-convert)
    rsvg-convert -w 2000 -b white "$LOGO_SVG" \
        -o "$OUTPUT_DIR/logo-chumbosoft-nuevo.png"

    echo "✓ PNG exportado con rsvg-convert"

else
    echo "❌ ERROR: No se encontró ningún conversor de SVG"
    echo ""
    echo "Instala uno de los siguientes:"
    echo "  • Inkscape (recomendado):  sudo apt install inkscape"
    echo "  • ImageMagick:             sudo apt install imagemagick"
    echo "  • rsvg-convert:            sudo apt install librsvg2-bin"
    exit 1
fi

echo ""

# Copiar SVG original
cp "$LOGO_SVG" "$OUTPUT_DIR/logo-chumbosoft-nuevo.svg"
echo "✓ SVG copiado"

# Copiar documentación
cp /home/juan/Documentos/IdeaProjects/chumbo.io/comparativa-logos-chumbosoft.pdf \
   "$OUTPUT_DIR/"
echo "✓ PDF comparativo copiado"

echo ""
echo "═══════════════════════════════════════════════"
echo "  Archivos listos para enviar a Apple Inc."
echo "═══════════════════════════════════════════════"
echo ""
echo "Directorio: $OUTPUT_DIR"
echo ""
ls -lh "$OUTPUT_DIR"
echo ""
echo "📧 Enviar estos archivos a: mcorbal@ga-p.com"
echo ""
echo "Archivos a adjuntar en el email:"
echo "  1. carta-respuesta.pdf (crear desde CARTA-RESPUESTA-APPLE.md)"
echo "  2. comparativa-logos-chumbosoft.pdf"
echo "  3. logo-chumbosoft-nuevo.svg"
echo "  4. logo-chumbosoft-nuevo.png"
echo ""

