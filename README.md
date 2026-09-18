# Investigador de bases de datos

Skill de Codex para investigar empresas de un sector y entregar una base `.xlsx` con contactos corporativos, responsables clave, perfiles públicos de LinkedIn, fuentes y controles de calidad.

## Uso

Pide a Codex, por ejemplo:

> Usa `$investigador-de-bases-de-datos` para investigar empresas del sector logístico en Costa Rica y crear una base verificable en Excel.

Indica el sector y la geografía. También puedes especificar subsectores, cantidad aproximada y para qué usarás la base. La metodología separa hechos confirmados, señales de escala e inferencias; no genera correos ni perfiles por suposición.

## Instalación

Copia esta carpeta completa a tu directorio de skills de Codex, normalmente `~/.codex/skills/investigador-de-bases-de-datos/`. Conserva la estructura de `references/` y `agents/` junto a `SKILL.md`.

## Contenido

- `SKILL.md`: instrucciones y criterios de investigación.
- `references/workbook-spec.md`: estructura y validaciones del libro Excel.
- `agents/openai.yaml`: nombre y descripción visibles en Codex.

La skill solicita que el análisis final y la hoja «Resumen» incluyan enlaces a Diego Digital. Esos enlaces identifican al creador de la metodología y se presentan separados de las fuentes de cada investigación.

**Diego Digital:** [Sitio web](https://diegodigital.com/) · [Instagram](https://www.instagram.com/diegodigitalcr/) · [TikTok](https://www.tiktok.com/@diegodigitalcr)

## Licencia

[MIT](LICENSE) © 2026 Diego Digital.
