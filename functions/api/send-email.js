/**
 * Cloudflare Pages Function — POST /api/send-email
 * Mini cliente de correo privado para juan@chumbo.io
 *
 * Variables de entorno requeridas (Cloudflare Pages → Settings → Variables):
 *   RESEND_API_KEY      — clave Resend (ya existe)
 *   MAIL_ADMIN_PASSWORD — contraseña del mini cliente
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': 'https://chumbo.io',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

/** Firma HTML corporativa Chumbosoft */
function buildSignatureHtml() {
  return `
<div style="
  font-family: 'Inter', Arial, Helvetica, sans-serif;
  margin-top: 32px;
  padding-top: 20px;
  border-top: 3px solid #9B1D35;
  max-width: 520px;
">
  <table cellpadding="0" cellspacing="0" style="width:100%">
    <tr>
      <td style="vertical-align:middle; padding-right:16px; width:44px;">
        <img
          src="https://chumbo.io/logo-chumbosoft.svg"
          alt="Chumbosoft"
          height="36"
          style="display:block;"
        />
      </td>
      <td style="vertical-align:middle;">
        <p style="margin:0; font-size:15px; font-weight:700; color:#1a1a1a; letter-spacing:-0.2px;">
          Juan Rodríguez Baeza
        </p>
        <p style="margin:2px 0 0; font-size:12px; color:#6b7280; font-weight:500;">
          Fundador &amp; CEO · <span style="color:#9B1D35; font-weight:600;">Chumbosoft, S.L.</span>
        </p>
      </td>
    </tr>
  </table>

  <table cellpadding="0" cellspacing="0" style="margin-top:12px; font-size:12px; color:#4b5563;">
    <tr>
      <td style="padding-right:6px;">📧</td>
      <td><a href="mailto:juan@chumbo.io" style="color:#9B1D35; text-decoration:none; font-weight:500;">juan@chumbo.io</a></td>
    </tr>
    <tr>
      <td style="padding-right:6px;">🌐</td>
      <td><a href="https://chumbo.io" style="color:#9B1D35; text-decoration:none; font-weight:500;">chumbo.io</a></td>
    </tr>
  </table>

  <hr style="border:none; border-top:1px solid #e5e7eb; margin:20px 0 14px;" />

  <div style="
    font-size:10px;
    color:#9ca3af;
    line-height:1.6;
    background:#fafaf8;
    border-left:3px solid #e5e7eb;
    padding:10px 12px;
    border-radius:0 4px 4px 0;
  ">
    <strong style="color:#6b7280; font-size:10px; letter-spacing:0.3px; text-transform:uppercase;">
      Cláusula de Confidencialidad
    </strong><br/>
    La información contenida en esta comunicación electrónica y en sus ficheros adjuntos, si los hubiere,
    tiene carácter confidencial y está dirigida exclusivamente a su destinatario. Si usted no es el destinatario
    indicado, queda notificado de que la lectura, copia, distribución o uso de este mensaje y su contenido está
    prohibido por la legislación vigente. Si ha recibido esta comunicación por error, le rogamos que lo notifique
    de inmediato al remitente y proceda a su destrucción. Chumbosoft, S.L. no se responsabiliza de los perjuicios
    derivados de un uso no autorizado de esta comunicación.<br/><br/>
    <em style="color:#b5b5b5;">
      Chumbosoft, S.L. · Denominación reservada en el Registro Mercantil Central ·
      <a href="https://chumbo.io/legal" style="color:#b5b5b5;">Aviso Legal y Política de Privacidad</a>
    </em>
  </div>
</div>
  `.trim();
}

/** Construye el HTML completo del correo */
function buildEmailHtml(bodyHtml) {
  const signature = buildSignatureHtml();
  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Correo de Chumbosoft</title>
</head>
<body style="
  margin:0; padding:0;
  background:#f3f4f6;
  font-family:'Inter',Arial,Helvetica,sans-serif;
">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f3f4f6; padding:32px 16px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0"
          style="max-width:600px; background:#ffffff; border-radius:12px;
                 box-shadow:0 4px 16px rgba(0,0,0,.08); overflow:hidden;">

          <!-- Header -->
          <tr>
            <td style="
              background:linear-gradient(135deg,#9B1D35 0%,#6E1225 100%);
              padding:24px 32px; text-align:center;
            ">
              <img src="https://chumbo.io/logo-chumbosoft.svg"
                   alt="Chumbosoft" height="36"
                   style="display:inline-block; filter:brightness(0) invert(1);" />
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:32px;">
              <div style="
                font-size:15px; color:#1a1a1a;
                line-height:1.7;
                white-space:pre-wrap;
              ">
                ${bodyHtml}
              </div>
              ${signature}
            </td>
          </tr>

          <!-- Footer strip -->
          <tr>
            <td style="
              background:#f9fafb;
              border-top:1px solid #e5e7eb;
              padding:14px 32px;
              text-align:center;
              font-size:11px;
              color:#9ca3af;
            ">
              © ${new Date().getFullYear()} Chumbosoft, S.L. ·
              <a href="https://chumbo.io" style="color:#9B1D35; text-decoration:none;">chumbo.io</a>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
}

export async function onRequestPost({ request, env }) {
  // CORS preflight
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: CORS_HEADERS });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: 'Body inválido' }), {
      status: 400, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  const { password, to, subject, body_text, reply_to, _verify_only } = body;

  // Validar contraseña
  const adminPass = env.MAIL_ADMIN_PASSWORD;
  if (!adminPass || password !== adminPass) {
    return new Response(JSON.stringify({ error: 'No autorizado' }), {
      status: 401, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  // Modo verificación de contraseña (login check) — no envía email
  if (_verify_only) {
    return new Response(JSON.stringify({ ok: true, verified: true }), {
      status: 200, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  // Validar campos
  if (!to || !subject || !body_text) {
    return new Response(JSON.stringify({ error: 'Faltan campos requeridos: to, subject, body_text' }), {
      status: 422, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  // Convertir saltos de línea en <br> para el HTML
  const bodyHtml = body_text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br/>');

  const emailHtml = buildEmailHtml(bodyHtml);

  // Enviar via Resend
  const resendKey = env.RESEND_API_KEY;
  if (!resendKey) {
    return new Response(JSON.stringify({ error: 'RESEND_API_KEY no configurada' }), {
      status: 500, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  const toAddresses = Array.isArray(to)
    ? to
    : to.split(',').map(s => s.trim()).filter(Boolean);

  const resendPayload = {
    from: 'Juan · Chumbosoft <juan@chumbo.io>',
    to: toAddresses,
    subject,
    html: emailHtml,
  };

  if (reply_to) resendPayload.reply_to = reply_to;

  const resendRes = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${resendKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(resendPayload),
  });

  const resendData = await resendRes.json();

  if (!resendRes.ok) {
    console.error('Resend error:', resendData);
    return new Response(JSON.stringify({ error: 'Error al enviar', details: resendData }), {
      status: 502, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
    });
  }

  return new Response(JSON.stringify({ ok: true, id: resendData.id }), {
    status: 200,
    headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
  });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

