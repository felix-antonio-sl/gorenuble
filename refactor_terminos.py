import re

mappings = {
    "ENT-ORG-FUNCIOANRIO": "ENT-ORG-FUNCIONARIO",
    "ENT-SYS-USER": "ENT-SYS-USUARIO",
    "ENT-TERR-ZONA-REZAGADA": "ENT-TERR-ZONA-REZAGO",
    "ENT-TDE-DOC-DIG": "ENT-TDE-DOCUMENTO-DIGITAL",
    "ENT-NORM-REPORTE-PMG": "ENT-NORM-INDICADOR-PMG",
    "ENT-DIG-EXPEDIENTE": "ENT-TDE-EXPEDIENTE-ELECTRONICO",
    "ENT-DIG-TOMA_RAZON": "ENT-TDE-INTEROP-CGR",
    "ENT-SYS-FIRMA-ELECTRONICA": "ENT-TDE-FIRMA-AVANZADA",
    "ENT-DIG-CONSENTIMIENTO": "ENT-TDE-CONSENTIMIENTO-INTEROP",
    "ENT-ORG-CAPACIDAD-INSTITUCIONAL": "ENT-ORKO-CAPACITY",
    "ENT-SYS-ADR": "ENT-ORKO-DECISION-LOG",
    "ENT-ORG-PROCESO-INTERNO": "ENT-ORKO-FLOW",
    "ENT-PLAN-STORY": "ENT-ORKO-USER-STORY",
    "ENT-SYS-FORMULARIO-F2": "ENT-FIN-FORMULARIO-F2-IDI",
    "ENT-DIG-DOCUMENTO": "ENT-TDE-DOCUMENTO-DIGITAL",
    "ENT-ORG-BRECHA-COMPETENCIA": "ENT-ORKO-CAPACITY-GAP",
    "ENT-SYS-BLUEPRINT-MODELO": "ENT-ORKO-BLUEPRINT",
    "ENT-TDE-PISEE-CONREQ": "ENT-TDE-PISEE-REQUEST",
    "ENT-SYS-TRAZABILIDAD-ACTO": "ENT-TDE-TRAZABILIDAD-LOG",
    "ENT-ORG-ROL": "ENT-GOB-ROL-INSTITUCIONAL",
}

input_file = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/terminos.md"
)
output_file = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/terminos.md"
)

with open(input_file, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    term = line.strip()
    if not term:
        continue

    # Apply specific mappings first
    if term in mappings:
        term = mappings[term]

    # Replace _ with -
    term = term.replace("_", "-")

    # Normalization rules
    term = term.replace("ENT-GOV-", "ENT-GOB-")
    term = term.replace("ENT-EJEC-", "ENT-EJE-")
    term = term.replace("ENT-LOC-", "ENT-TERR-")

    # Special case for ENT-TER-SITIO -> ENT-TERR-SITIO
    if term.startswith("ENT-TER-"):
        term = term.replace("ENT-TER-", "ENT-TERR-")

    new_lines.append(term)

# Remove duplicates while preserving order (or sort if preferred)
# User might want them sorted for better organization
seen = set()
unique_lines = []
for line in new_lines:
    if line not in seen:
        unique_lines.append(line)
        seen.add(line)

unique_lines.sort()

with open(output_file, "w") as f:
    for line in unique_lines:
        f.write(line + "\n")
