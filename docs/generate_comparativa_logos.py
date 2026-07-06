#!/usr/bin/env python3
"""
Genera una comparativa visual entre el logo antiguo (con mordisco)
y el nuevo logo rediseñado (sin mordisco) de CHUMBOSOFT.

Este PDF se usará como anexo en la comunicación con Apple Inc.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os

# Colores corporativos CHUMBOSOFT
COLOR_ROJO = HexColor('#9B1D35')
COLOR_NARANJA = HexColor('#F4A523')
COLOR_GRIS_OSCURO = HexColor('#333333')
COLOR_GRIS_CLARO = HexColor('#666666')

def crear_comparativa_logos(output_path='comparativa-logos-chumbosoft.pdf'):
    """
    Crea un PDF comparativo entre el logo antiguo y el nuevo.
    """
    # Crear canvas
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # ═══════════════════════════════════════════════════
    # PÁGINA 1: Portada e Introducción
    # ═══════════════════════════════════════════════════

    # Título principal
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_ROJO)
    c.drawCentredString(width/2, height - 4*cm, "REDISEÑO DE MARCA")

    c.setFont("Helvetica", 18)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawCentredString(width/2, height - 5*cm, "CHUMBOSOFT")

    # Línea decorativa
    c.setStrokeColor(COLOR_NARANJA)
    c.setLineWidth(2)
    c.line(width/2 - 8*cm, height - 5.5*cm, width/2 + 8*cm, height - 5.5*cm)

    # Información del documento
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(width/2, height - 7*cm, "Comparativa de Diseño Original vs. Rediseñado")
    c.drawCentredString(width/2, height - 7.7*cm, "Solicitud de Marca: M4372984(3)")
    c.drawCentredString(width/2, height - 8.4*cm, "Fecha: 6 de julio de 2026")

    # Cuadro de resumen
    y_pos = height - 11*cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, y_pos, "RESUMEN DE CAMBIOS:")

    y_pos -= 1.2*cm
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_GRIS_OSCURO)

    cambios = [
        "✗  ELIMINADO: Mordisco en el lado derecho de la fruta",
        "✗  ELIMINADO: Hoja inclinada hacia la derecha",
        "✗  ELIMINADO: Forma similar a manzana",
        "",
        "✓  AÑADIDO: Forma ovalada vertical (higo chumbo)",
        "✓  AÑADIDO: Corona floral en la parte superior",
        "✓  AÑADIDO: Patrón distintivo de aréolas",
        "",
        "✓  CONSERVADO: Colores corporativos (#9B1D35 y #F4A523)",
        "✓  CONSERVADO: Denominación 'CHUMBOSOFT'",
    ]

    for cambio in cambios:
        c.drawString(4.5*cm, y_pos, cambio)
        y_pos -= 0.7*cm

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(width/2, 2*cm, "Documento preparado para Apple Inc.")
    c.drawCentredString(width/2, 1.5*cm, "chumbo.io | juan@chumbo.io | +34 625 993 716")

    c.showPage()

    # ═══════════════════════════════════════════════════
    # PÁGINA 2: Análisis de Similitudes (ANTES)
    # ═══════════════════════════════════════════════════

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_ROJO)
    c.drawCentredString(width/2, height - 3*cm, "DISEÑO ORIGINAL")
    c.setFont("Helvetica", 12)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawCentredString(width/2, height - 3.8*cm, "(Solicitud M4372984(3) - 7 de abril de 2026)")

    # Línea
    c.setStrokeColor(COLOR_NARANJA)
    c.line(4*cm, height - 4.3*cm, width - 4*cm, height - 4.3*cm)

    y_pos = height - 6*cm
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, y_pos, "PROBLEMAS IDENTIFICADOS:")

    y_pos -= 1.5*cm
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_GRIS_OSCURO)

    problemas = [
        "1. MORDISCO EN EL LADO DERECHO",
        "   • Similar al característico 'bite' del logo de Apple",
        "   • Creado mediante una máscara circular (circle cx='163' cy='116' r='36')",
        "   • Posicionado en la misma zona que el logo de Apple",
        "",
        "2. HOJA INCLINADA HACIA LA DERECHA",
        "   • Orientación similar a la hoja del logo de Apple",
        "   • El código SVG original incluía comentarios: 'Tallito + hojita estilo Apple'",
        "   • Ángulo y posición coincidentes",
        "",
        "3. FORMA GENERAL DE MANZANA",
        "   • Clasificación de Viena: 05.07.13 (manzanas)",
        "   • Forma redondeada similar a una manzana",
        "   • Proporciones similares al logo de Apple",
        "",
        "4. RIESGO DE CONFUSIÓN",
        "   • Consumidores podrían asociar el logo con Apple",
        "   • Uso en Clase 42 (misma clase que Apple para servicios de software)",
        "   • Posible dilución de la marca Apple",
    ]

    for prob in problemas:
        c.drawString(4.5*cm, y_pos, prob)
        y_pos -= 0.6*cm

    # Nota al pie
    c.setFont("Helvetica-BoldOblique", 10)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, 3*cm, "CONCLUSIÓN:")
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(4.5*cm, 2.4*cm, "El diseño original presentaba similitudes significativas con el logo de Apple que")
    c.drawString(4.5*cm, 1.9*cm, "podrían causar confusión en el mercado. Procedimos a un rediseño completo.")

    c.showPage()

    # ═══════════════════════════════════════════════════
    # PÁGINA 3: Nuevo Diseño (DESPUÉS)
    # ═══════════════════════════════════════════════════

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor('#00AA00'))  # Verde para "aprobado"
    c.drawCentredString(width/2, height - 3*cm, "DISEÑO REDISEÑADO")
    c.setFont("Helvetica", 12)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawCentredString(width/2, height - 3.8*cm, "(Versión 2.0 - 6 de julio de 2026)")

    # Línea
    c.setStrokeColor(COLOR_NARANJA)
    c.line(4*cm, height - 4.3*cm, width - 4*cm, height - 4.3*cm)

    y_pos = height - 6*cm
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor('#00AA00'))
    c.drawString(4*cm, y_pos, "SOLUCIONES IMPLEMENTADAS:")

    y_pos -= 1.5*cm
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_GRIS_OSCURO)

    soluciones = [
        "1. ELIMINACIÓN TOTAL DEL MORDISCO",
        "   ✓ El nuevo diseño NO incluye ningún mordisco",
        "   ✓ Forma completa de elipse (ellipse cx='100' cy='130' rx='48' ry='80')",
        "   ✓ Sin máscaras que creen mordeduras",
        "",
        "2. CORONA FLORAL EN LUGAR DE HOJA",
        "   ✓ Corona floral con 3 pétalos en la parte superior",
        "   ✓ Característica única del higo chumbo (tuna/nopal)",
        "   ✓ Orientación central, no lateral",
        "   ✓ Completamente diferente a la hoja de Apple",
        "",
        "3. FORMA DE HIGO CHUMBO",
        "   ✓ Forma ovalada vertical (no circular como manzana)",
        "   ✓ Proporciones rx=48, ry=80 (más alargada)",
        "   ✓ Nueva clasificación de Viena esperada: 05.11 (otros frutos)",
        "   ✓ NO clasificará como manzana (05.07.13)",
        "",
        "4. ELEMENTOS DISTINTIVOS ADICIONALES",
        "   ✓ Patrón ampliado de aréolas (textura de cactus)",
        "   ✓ Corona floral con detalles en color naranja",
        "   ✓ Diseño que representa claramente un fruto de cactus",
        "",
        "5. SIN RIESGO DE CONFUSIÓN",
        "   ✓ Diseño completamente diferente al logo de Apple",
        "   ✓ No puede confundirse con una manzana",
        "   ✓ Identidad única y distintiva",
        "   ✓ Mantiene coherencia con la marca 'CHUMBOSOFT'",
    ]

    for sol in soluciones:
        c.drawString(4.5*cm, y_pos, sol)
        y_pos -= 0.55*cm

    # Nota al pie
    c.setFont("Helvetica-BoldOblique", 10)
    c.setFillColor(HexColor('#00AA00'))
    c.drawString(4*cm, 2.5*cm, "CONCLUSIÓN:")
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(4.5*cm, 1.9*cm, "El nuevo diseño elimina completamente cualquier similitud con el logo de Apple,")
    c.drawString(4.5*cm, 1.4*cm, "representando de forma única y distintiva nuestra identidad basada en el higo chumbo.")

    c.showPage()

    # ═══════════════════════════════════════════════════
    # PÁGINA 4: Comparativa Lado a Lado
    # ═══════════════════════════════════════════════════

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_ROJO)
    c.drawCentredString(width/2, height - 3*cm, "COMPARATIVA LADO A LADO")

    # Línea
    c.setStrokeColor(COLOR_NARANJA)
    c.line(4*cm, height - 3.5*cm, width - 4*cm, height - 3.5*cm)

    # Divisor vertical
    c.setStrokeColor(COLOR_GRIS_CLARO)
    c.setLineWidth(1)
    c.line(width/2, height - 5*cm, width/2, height - 22*cm)

    # Columna izquierda: ANTES
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ROJO)
    c.drawCentredString(width/4, height - 5*cm, "ANTES")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(width/4, height - 5.7*cm, "(Diseño con mordisco)")

    # Aquí iría la imagen del logo antiguo
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(width/4, height - 12*cm, "[Logo antiguo con mordisco]")
    c.drawCentredString(width/4, height - 12.7*cm, "Ver archivo adjunto:")
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/4, height - 13.4*cm, "logo-chumbosoft-antiguo.svg")

    # Características ANTES
    y_pos = height - 15*cm
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(width/4 - 3*cm, y_pos, "Características:")
    y_pos -= 0.7*cm
    c.setFont("Helvetica", 9)
    caracteristicas_antes = [
        "✗ Con mordisco lateral",
        "✗ Hoja inclinada derecha",
        "✗ Forma de manzana",
        "✗ Viena: 05.07.13",
    ]
    for car in caracteristicas_antes:
        c.drawString(width/4 - 3*cm, y_pos, car)
        y_pos -= 0.5*cm

    # Columna derecha: DESPUÉS
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor('#00AA00'))
    c.drawCentredString(3*width/4, height - 5*cm, "DESPUÉS")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(3*width/4, height - 5.7*cm, "(Diseño rediseñado)")

    # Aquí iría la imagen del logo nuevo
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(3*width/4, height - 12*cm, "[Logo nuevo sin mordisco]")
    c.drawCentredString(3*width/4, height - 12.7*cm, "Ver archivo adjunto:")
    c.setFont("Helvetica", 9)
    c.drawCentredString(3*width/4, height - 13.4*cm, "logo-chumbosoft.svg")

    # Características DESPUÉS
    y_pos = height - 15*cm
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(3*width/4 - 3*cm, y_pos, "Características:")
    y_pos -= 0.7*cm
    c.setFont("Helvetica", 9)
    caracteristicas_despues = [
        "✓ SIN mordisco",
        "✓ Corona floral superior",
        "✓ Forma de higo chumbo",
        "✓ Viena: 05.11 (esperada)",
    ]
    for car in caracteristicas_despues:
        c.drawString(3*width/4 - 3*cm, y_pos, car)
        y_pos -= 0.5*cm

    # Nota final
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, height - 24*cm, "DIFERENCIAS CLAVE:")

    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    diferencias = [
        "• El mordisco ha sido completamente eliminado → No hay similitud con Apple",
        "• La hoja lateral ha sido sustituida por corona floral central → Distintivo único",
        "• La forma ha cambiado de manzana circular a higo chumbo ovalado → Diferenciación clara",
        "• Se añadieron elementos únicos del fruto del cactus → Identidad propia",
    ]

    y_pos = height - 25*cm
    for dif in diferencias:
        c.drawString(4.5*cm, y_pos, dif)
        y_pos -= 0.7*cm

    c.showPage()

    # ═══════════════════════════════════════════════════
    # PÁGINA 5: Conclusiones y Próximos Pasos
    # ═══════════════════════════════════════════════════

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_ROJO)
    c.drawCentredString(width/2, height - 3*cm, "CONCLUSIONES Y COMPROMISO")

    # Línea
    c.setStrokeColor(COLOR_NARANJA)
    c.line(4*cm, height - 3.5*cm, width - 4*cm, height - 3.5*cm)

    y_pos = height - 5.5*cm

    # Sección 1: Acciones completadas
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor('#00AA00'))
    c.drawString(4*cm, y_pos, "1. ACCIONES COMPLETADAS (6 de julio de 2026):")

    y_pos -= 1*cm
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    acciones = [
        "✓ Rediseño completo del logo eliminando toda similitud con Apple",
        "✓ Actualización de todos los activos corporativos (web, tarjetas, etc.)",
        "✓ Cese inmediato del uso del diseño anterior",
        "✓ Preparación de documentación para Apple Inc.",
    ]

    for acc in acciones:
        c.drawString(4.5*cm, y_pos, acc)
        y_pos -= 0.7*cm

    y_pos -= 1*cm

    # Sección 2: Próximos pasos
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, y_pos, "2. PRÓXIMOS PASOS:")

    y_pos -= 1*cm
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    proximos = [
        "1. Enviar este documento y el nuevo diseño a Apple Inc. para su revisión",
        "2. Esperar aprobación de Apple Inc. del nuevo diseño",
        "3. Presentar desistimiento de la solicitud M4372984(3) ante la OEPM",
        "4. Presentar nueva solicitud con el diseño rediseñado una vez aprobado",
    ]

    for prox in proximos:
        c.drawString(4.5*cm, y_pos, prox)
        y_pos -= 0.7*cm

    y_pos -= 1*cm

    # Sección 3: Garantías
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, y_pos, "3. GARANTÍAS:")

    y_pos -= 1*cm
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    garantias = [
        "• El nuevo diseño NO presenta similitud con el logo de Apple",
        "• NO existe riesgo de confusión para los consumidores",
        "• NO puede dar lugar a dilución de las marcas de Apple",
        "• Representa de forma única y distintiva nuestra identidad (higo chumbo)",
        "• Respeta plenamente los derechos de propiedad industrial de Apple Inc.",
    ]

    for gar in garantias:
        c.drawString(4.5*cm, y_pos, gar)
        y_pos -= 0.7*cm

    # Cuadro de firma
    y_pos = 8*cm
    c.setStrokeColor(COLOR_NARANJA)
    c.setLineWidth(1.5)
    c.rect(4*cm, y_pos - 4*cm, width - 8*cm, 4*cm)

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4.5*cm, y_pos - 1*cm, "SOLICITAMOS:")

    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(4.5*cm, y_pos - 1.8*cm, "Confirmación por parte de Apple Inc. de que el nuevo diseño adjunto")
    c.drawString(4.5*cm, y_pos - 2.4*cm, "es aceptable y no presenta objeciones, para proceder con seguridad")
    c.drawString(4.5*cm, y_pos - 3*cm, "jurídica al desistimiento y nueva solicitud.")

    # Contacto
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_ROJO)
    c.drawString(4*cm, 4.5*cm, "CONTACTO:")

    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_GRIS_OSCURO)
    c.drawString(4.5*cm, 3.8*cm, "Juan Antonio Rodríguez Baeza")
    c.drawString(4.5*cm, 3.3*cm, "Email: juan@chumbo.io")
    c.drawString(4.5*cm, 2.8*cm, "Teléfono: +34 625 993 716")
    c.drawString(4.5*cm, 2.3*cm, "Web: chumbo.io")

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(COLOR_GRIS_CLARO)
    c.drawCentredString(width/2, 1.5*cm, "Madrid, 6 de julio de 2026")
    c.drawCentredString(width/2, 1*cm, "Este documento ha sido preparado en respuesta al burofax recibido de GA_P en nombre de Apple Inc.")

    # Guardar PDF
    c.save()

    print(f"✓ PDF creado exitosamente: {output_path}")
    return output_path


if __name__ == "__main__":
    # Directorio de salida
    output_dir = os.path.join(os.path.dirname(__file__), "..")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "comparativa-logos-chumbosoft.pdf")

    print("Generando comparativa de logos...")
    pdf_path = crear_comparativa_logos(output_file)

    print(f"\n{'='*60}")
    print(f"PDF generado: {pdf_path}")
    print(f"{'='*60}")
    print("\nEste PDF debe ser enviado a Apple Inc. junto con:")
    print("  • Carta de respuesta al burofax")
    print("  • Archivo SVG del nuevo logo (logo-chumbosoft.svg)")
    print("\nContacto Apple (GA_P):")
    print("  • Email: mcorbal@ga-p.com")
    print("  • Teléfono: 91 582 91 00")

