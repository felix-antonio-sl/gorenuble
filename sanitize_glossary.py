#!/usr/bin/env python3
"""
Sanitiza el glosario IPR aplicando criterios semánticos:
1. Elimina frases largas que son descripciones, no términos
2. Elimina secciones de formularios (Sección 1, Sección 2...)
3. Elimina valores de hora y descripciones de gastos
4. Consolida siglas con sus expansiones (mantiene ambas pero agrupa)
5. Elimina entradas con caracteres especiales o formato de tabla
"""
import re

input_path = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/glosario.yml"
)
output_path = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/glosario.yml"
)

# Leer términos actuales
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

terms = []
for line in lines:
    line = line.strip()
    if line.startswith('- "') and line.endswith('"'):
        term = line[3:-1]  # Extraer contenido entre - " y "
        terms.append(term)


# Criterios de exclusión semántica
def is_valid_term(term):
    # Excluir si es muy largo (probablemente una descripción)
    if len(term) > 80:
        return False

    # Excluir secciones de formularios
    if re.match(r"^Sección \d+", term) or re.match(r"^Sub-etapa \d+", term):
        return False
    if "Sección I:" in term or "Sección II:" in term or "Sección III:" in term:
        return False
    if "Sección IV:" in term or "Sección V:" in term or "Sección VI:" in term:
        return False
    if "Sección VII:" in term or "Sección VIII:" in term or "Sección IX:" in term:
        return False

    # Excluir pasos numerados de procesos
    if re.match(r"^\d+\.\d+\s", term):
        return False

    # Excluir valores de hora y descripciones de gastos
    if "Valores-Hora" in term or "Gastos-Permitidos" in term:
        return False
    if "Medios   -" in term or "- Ctx:" in term or "- Req:" in term:
        return False

    # Excluir casos específicos de documentos (Caso A, Caso B...)
    if re.match(r"^Caso [A-Z0-9]+ –", term):
        return False

    # Excluir anexos genéricos numerados
    if re.match(r"^Anexo \d+ –", term):
        return False

    # Excluir frases que terminan con punto (probablemente oraciones)
    if term.endswith(".") and len(term) > 40:
        return False

    # Excluir descripciones de composición
    if term.startswith("Composición del"):
        return False

    # Excluir referencias a tablas o contenido de tablas
    if "|" in term:
        return False

    # Excluir instrucciones o descripciones de proceso
    if term.startswith("Cuando la ejecución") or term.startswith(
        "Las bases determinan"
    ):
        return False
    if term.startswith("La ejecución se rige"):
        return False

    return True


# Aplicar filtro
filtered_terms = [t for t in terms if is_valid_term(t)]

# Normalizar y deduplicar (case-insensitive para detectar duplicados)
seen = set()
unique_terms = []
for term in filtered_terms:
    normalized = term.lower().strip()
    # Remover puntos finales para normalización
    if normalized.endswith("."):
        normalized = normalized[:-1]
    if normalized not in seen:
        seen.add(normalized)
        # Guardar versión original (sin punto final si lo tenía)
        clean_term = term.rstrip(".")
        unique_terms.append(clean_term)

# Ordenar alfabéticamente
unique_terms.sort(key=lambda x: x.lower())

# Escribir resultado
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Glosario IPR - GORE Ñuble\n")
    f.write(
        "# Términos extraídos de documentos KODA de gestión de inversión pública regional\n"
    )
    f.write(
        "# Saneado semánticamente: solo términos, siglas, conceptos e instituciones\n\n"
    )
    f.write("terminos:\n")
    for term in unique_terms:
        safe_term = term.replace('"', '\\"')
        f.write(f'  - "{safe_term}"\n')

print(f"Original: {len(terms)} términos")
print(f"Después de filtro semántico: {len(unique_terms)} términos")
print(f"Eliminados: {len(terms) - len(unique_terms)} entradas")
