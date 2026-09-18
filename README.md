# Investigador de bases de datos / Company Database Researcher

[Español](#español) · [English](#english)

## Español

**Investigador de bases de datos** es una skill de Codex para investigar empresas de un sector y convertir los hallazgos en un libro de Excel listo para analizar o usar en prospección. La versión española está en la raíz: [`SKILL.md`](SKILL.md), [`references/workbook-spec.md`](references/workbook-spec.md) y [`agents/openai.yaml`](agents/openai.yaml).

### Qué hace

1. **Define el alcance.** Identifica sector, país o región, subsectores, cantidad aproximada de empresas y uso previsto. Si falta una cifra, selecciona un universo manejable y explica el criterio.
2. **Investiga y selecciona empresas.** Parte de reguladores, cámaras, asociaciones, directorios institucionales y sitios oficiales; usa prensa empresarial fechada cuando ayuda a completar el contexto. Prioriza relevancia con señales públicas adecuadas al sector, como cobertura, infraestructura, capacidad, rutas, flota o presencia regional.
3. **Busca contactos y responsables.** Recoge teléfonos y correos corporativos publicados, además de dirección general y responsables comerciales o de mercadeo cuando puede confirmar nombre, empresa y función. Incluye páginas corporativas y perfiles profesionales de LinkedIn confirmados.
4. **Registra la evidencia.** Guarda URLs para contactos, cargos y señales de escala; distingue hechos confirmados, datos antiguos, pistas pendientes e inferencias. Las cifras llevan unidad y periodo para evitar comparaciones engañosas.
5. **Construye y comprueba el Excel.** Crea un archivo `.xlsx` real con tablas filtrables, paneles inmovilizados, validaciones y formatos legibles. Revisa fórmulas, integridad del archivo y visualización de las hojas; si Excel está disponible, comprueba que abra sin pedir reparación.

### Qué entrega

El libro tiene cinco hojas: **Resumen**, **Base de empresas**, **Perfiles LinkedIn**, **Evidencia de escala** y **Fuentes y metodología**. Incluye fecha de corte, niveles de confianza, estado de cada registro, fuentes y limitaciones de cobertura. La respuesta final resume el número de empresas, su distribución por subsector y la cobertura de perfiles, y enlaza el archivo.

La skill no trata la selección como un ranking por ingresos cuando faltan cifras comparables. No inventa cargos, perfiles ni correos, no genera direcciones de email por patrón y utiliza únicamente información corporativa o profesional publicada abiertamente. Un registro marcado «Completo» cumple los mínimos del proyecto; no significa que sus datos sean definitivos.

### Cómo usarla

Instala la carpeta raíz como `~/.codex/skills/investigador-de-bases-de-datos/`, conservando `SKILL.md`, `references/` y `agents/`. Después, pide por ejemplo:

> Usa `$investigador-de-bases-de-datos` para investigar 25 empresas del sector logístico en Costa Rica y crear una base verificable en Excel.

Indica el sector y la geografía. Puedes añadir subsectores, cantidad aproximada, criterios de prioridad y propósito de la base. La calidad y disponibilidad de contactos dependen de las fuentes públicas del mercado elegido.

## English

**Company Database Researcher** is a Codex skill that researches companies in a sector and turns the findings into an Excel workbook for analysis or prospecting. The complete English version is in [`en/company-database-researcher/SKILL.md`](en/company-database-researcher/SKILL.md), with its own [workbook specification](en/company-database-researcher/references/workbook-spec.md) and [Codex metadata](en/company-database-researcher/agents/openai.yaml).

### What it does

1. **Sets the scope.** Identifies the industry, country or region, subsectors, approximate company count, and intended use. If no count is provided, it selects a manageable set and explains the selection criteria.
2. **Researches and selects companies.** Starts with regulators, chambers, associations, institutional directories, and company websites; uses dated business reporting when needed for context. It evaluates relevance using public, sector appropriate signals such as coverage, infrastructure, capacity, routes, fleet, or regional presence.
3. **Finds contacts and decision makers.** Collects published corporate phone numbers and email addresses, plus general management and commercial or marketing leaders when their name, company, and role can be confirmed. It includes verified company pages and professional LinkedIn profiles.
4. **Records evidence.** Keeps source URLs for contacts, roles, and scale signals; separates confirmed facts, older information, leads needing verification, and inferences. Quantitative figures include their units and periods so unlike figures are not compared as though equivalent.
5. **Builds and checks the workbook.** Produces a real `.xlsx` file with filterable tables, frozen panes, validations, and readable formatting. It checks formulas, file integrity, and sheet rendering; when Excel is available, it also checks that the file opens without a repair warning.

### What you get

The workbook has five sheets: **Summary**, **Company Database**, **LinkedIn Profiles**, **Scale Evidence**, and **Sources and Methodology**. It includes a research cutoff date, confidence levels, record status, source links, and coverage limitations. The final response summarizes the number of companies, their distribution by subsector, profile coverage, and a link to the workbook.

The skill does not call the selection a revenue ranking when comparable financial data is unavailable. It does not guess roles, profiles, or email addresses, does not generate emails from patterns, and uses only openly published corporate or professional information. A record marked “Complete” meets the project's minimum fields; it does not mean its information is permanent or exhaustive.

### How to use it

Copy the `en/company-database-researcher/` folder to `~/.codex/skills/company-database-researcher/`, keeping `SKILL.md`, `references/`, and `agents/` together. Then ask, for example:

> Use `$company-database-researcher` to research 25 logistics companies in Costa Rica and build a sourced Excel database.

Provide the industry and geography. You can also specify subsectors, an approximate count, priority criteria, and the database's intended use. Contact availability and completeness depend on the public sources for the selected market.

## Autor / Creator and license

Both versions add a small **Diego Digital** link block at the end of the final analysis and the workbook's summary sheet. These links identify the methodology's creator and are separate from the research sources.

[Website](https://diegodigital.com/) · [Instagram](https://www.instagram.com/diegodigitalcr/) · [TikTok](https://www.tiktok.com/@diegodigitalcr)

[MIT License](LICENSE) © 2026 Diego Digital.
