#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor de Glosario Terminológico desde Ontologías TTL
=========================================================
Extrae entidades (clases, propiedades, instancias) con sus definiciones SKOS
desde archivos Turtle (.ttl) y genera un glosario en formato Markdown.

Autor: KODA-TRANSFORMER
Fecha: 2026-01-27
"""

import re
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

ONTOLOGY_PATHS = [
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/ontologies/onto_gorenuble",
    "/Users/felixsanhueza/Developer/tde/knowledge/ontologies/onto_tde",
]

OUTPUT_PATH = "/Users/felixsanhueza/Developer/gorenuble/docs/glosario_terminologico.md"

# Archivos a excluir (datos de instancias, no definiciones)
EXCLUDE_PATTERNS = [
    "*Data.ttl",
    "*Instances.ttl",
    "*Rules.ttl",
    "*Shapes.ttl",
    "catalog-*.xml",
    "*Bundle.ttl",
]

# ============================================================================
# PARSER TTL SIMPLIFICADO
# ============================================================================


def should_exclude(filename: str) -> bool:
    """Verifica si un archivo debe ser excluido."""
    import fnmatch

    for pattern in EXCLUDE_PATTERNS:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def extract_prefixes(content: str) -> dict:
    """Extrae prefijos del archivo TTL."""
    prefixes = {}
    for match in re.finditer(r"@prefix\s+(\w+):\s+<([^>]+)>", content):
        prefixes[match.group(1)] = match.group(2)
    return prefixes


def expand_uri(uri: str, prefixes: dict) -> str:
    """Expande un URI con prefijo a su forma completa."""
    if ":" in uri and not uri.startswith("http"):
        prefix, local = uri.split(":", 1)
        if prefix in prefixes:
            return prefixes[prefix] + local
    return uri


def get_local_name(uri: str) -> str:
    """Obtiene el nombre local de un URI."""
    if "#" in uri:
        return uri.split("#")[-1]
    return uri.split("/")[-1]


def extract_entities(content: str, prefixes: dict) -> list:
    """Extrae entidades con sus anotaciones SKOS del contenido TTL."""
    entities = []

    # Patrón para encontrar bloques de definición de entidades
    # Busca: prefijo:NombreLocal seguido de propiedades
    entity_pattern = r"(\w+:\w+)\s*\n?\s*a\s+owl:Class\s*[;.]([^\.]*(?:\.\s*\n\n|\Z))"

    # Patrón más flexible para cualquier entidad con skos:definition
    block_pattern = r"((?:\w+:\w+)|(?:<[^>]+>))\s*\n?\s*(?:a\s+[^;]+\s*;\s*)?(?:[^\.]*?)(skos:definition\s+[^;]+)"

    # Extraer bloques completos separados por líneas en blanco o punto final
    blocks = re.split(r"\n\s*\n+(?=[a-zA-Z<])", content)

    for block in blocks:
        block = block.strip()
        if not block or block.startswith("#") or block.startswith("@"):
            continue

        entity = parse_entity_block(block, prefixes)
        if entity and entity.get("definition"):
            entities.append(entity)

    return entities


def parse_entity_block(block: str, prefixes: dict) -> dict:
    """Parsea un bloque de entidad y extrae sus anotaciones."""
    lines = block.strip().split("\n")
    if not lines:
        return None

    # Obtener el URI de la entidad (primera línea)
    first_line = lines[0].strip()
    uri_match = re.match(r"^(\w+:\w+|<[^>]+>)", first_line)
    if not uri_match:
        return None

    raw_uri = uri_match.group(1).strip("<>")
    if raw_uri.startswith("http"):
        uri = raw_uri
    else:
        uri = expand_uri(raw_uri, prefixes)

    entity = {
        "uri": uri,
        "local_name": get_local_name(uri),
        "type": None,
        "prefLabel": None,
        "prefLabel_en": None,
        "definition": None,
        "example": None,
        "note": None,
        "scopeNote": None,
        "altLabel": None,
        "source_ontology": None,
    }

    # Detectar tipo
    if "a owl:Class" in block or "a owl:class" in block:
        entity["type"] = "Class"
    elif "a owl:ObjectProperty" in block:
        entity["type"] = "ObjectProperty"
    elif "a owl:DatatypeProperty" in block:
        entity["type"] = "DatatypeProperty"
    elif "a gist:Aspect" in block:
        entity["type"] = "Aspect"
    elif "a owl:Ontology" in block:
        entity["type"] = "Ontology"
    else:
        # Buscar cualquier tipo
        type_match = re.search(r"a\s+(\w+:\w+)", block)
        if type_match:
            entity["type"] = type_match.group(1)

    # Extraer rdfs:isDefinedBy
    defined_match = re.search(r"rdfs:isDefinedBy\s+<([^>]+)>", block)
    if defined_match:
        entity["source_ontology"] = get_local_name(defined_match.group(1))

    # Extraer anotaciones SKOS
    entity["prefLabel"] = extract_skos_annotation(block, "prefLabel", "@es")
    if not entity["prefLabel"]:
        entity["prefLabel"] = extract_skos_annotation(block, "prefLabel")
    entity["prefLabel_en"] = extract_skos_annotation(block, "prefLabel", "@en")
    entity["definition"] = extract_skos_annotation(block, "definition", "@es")
    if not entity["definition"]:
        entity["definition"] = extract_skos_annotation(block, "definition")
    entity["example"] = extract_skos_annotation(block, "example", "@es")
    if not entity["example"]:
        entity["example"] = extract_skos_annotation(block, "example")
    entity["note"] = extract_skos_annotation(block, "note", "@es")
    entity["scopeNote"] = extract_skos_annotation(block, "scopeNote", "@es")
    entity["altLabel"] = extract_skos_annotation(block, "altLabel", "@es")

    return entity


def extract_skos_annotation(block: str, annotation: str, lang_tag: str = None) -> str:
    """Extrae una anotación SKOS del bloque."""
    # Patrón para strings multilínea con """
    multi_pattern = rf'skos:{annotation}\s+"""([^"]*(?:""[^"]+)*?)"""'
    # Patrón para strings simples con "
    simple_pattern = rf'skos:{annotation}\s+"([^"]*)"'

    # Buscar con tag de idioma
    if lang_tag:
        multi_with_lang = (
            rf'skos:{annotation}\s+"""([^"]*(?:""[^"]+)*?)"""\s*{lang_tag}'
        )
        simple_with_lang = rf'skos:{annotation}\s+"([^"]+)"\s*{lang_tag}'

        match = re.search(multi_with_lang, block, re.DOTALL)
        if match:
            return clean_string(match.group(1))
        match = re.search(simple_with_lang, block)
        if match:
            return clean_string(match.group(1))

    # Buscar sin tag de idioma
    match = re.search(multi_pattern, block, re.DOTALL)
    if match:
        return clean_string(match.group(1))
    match = re.search(simple_pattern, block)
    if match:
        return clean_string(match.group(1))

    return None


def clean_string(s: str) -> str:
    """Limpia un string de caracteres de escape y espacios extra."""
    if not s:
        return None
    s = s.replace("\\n", " ")
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# ============================================================================
# GENERADOR DE MARKDOWN
# ============================================================================


def generate_markdown(entities: list, output_path: str):
    """Genera el archivo Markdown del glosario."""

    # Agrupar por ontología de origen
    by_ontology = defaultdict(list)
    for e in entities:
        source = e.get("source_ontology") or "Otros"
        by_ontology[source].append(e)

    # Ordenar cada grupo alfabéticamente por prefLabel
    for source in by_ontology:
        by_ontology[source].sort(
            key=lambda x: (x.get("prefLabel") or x.get("local_name") or "").lower()
        )

    # Generar Markdown
    lines = []
    lines.append("# Glosario Terminológico - Ontologías GORE Ñuble & TDE")
    lines.append("")
    lines.append(
        f"> **Generado automáticamente**: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    lines.append("> ")
    lines.append(
        "> Este glosario contiene las definiciones de clases, propiedades y aspectos"
    )
    lines.append("> extraídos de las ontologías GORE Ñuble y TDE del Estado de Chile.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Tabla de contenidos
    lines.append("## Tabla de Contenidos")
    lines.append("")
    for source in sorted(by_ontology.keys()):
        anchor = source.lower().replace(" ", "-").replace(".", "")
        lines.append(f"- [{source}](#{anchor}) ({len(by_ontology[source])} términos)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Secciones por ontología
    for source in sorted(by_ontology.keys()):
        lines.append(f"## {source}")
        lines.append("")

        for entity in by_ontology[source]:
            term = entity.get("prefLabel") or entity.get("local_name")
            term_en = entity.get("prefLabel_en")
            definition = entity.get("definition")
            etype = entity.get("type") or ""
            example = entity.get("example")
            note = entity.get("scopeNote") or entity.get("note")
            alt_label = entity.get("altLabel")

            # Encabezado del término
            type_badge = f" `{etype}`" if etype else ""
            en_suffix = f" / {term_en}" if term_en and term_en != term else ""
            lines.append(f"### {term}{en_suffix}{type_badge}")
            lines.append("")

            # URI como código
            lines.append(f"**URI**: `{entity.get('local_name')}`")
            lines.append("")

            # Alias
            if alt_label:
                lines.append(f"**Alias**: {alt_label}")
                lines.append("")

            # Definición
            if definition:
                lines.append(f"**Definición**: {definition}")
                lines.append("")

            # Ejemplo
            if example:
                lines.append(f"> **Ejemplo**: {example}")
                lines.append("")

            # Nota de alcance
            if note:
                lines.append(f"*Nota*: {note}")
                lines.append("")

            lines.append("---")
            lines.append("")

    # Estadísticas finales
    total = sum(len(v) for v in by_ontology.values())
    lines.append("## Estadísticas")
    lines.append("")
    lines.append(f"- **Total de términos**: {total}")
    for source in sorted(by_ontology.keys()):
        lines.append(f"- **{source}**: {len(by_ontology[source])} términos")
    lines.append("")

    # Escribir archivo
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Glosario generado: {output_path}")
    print(f"   Total: {total} términos")


# ============================================================================
# MAIN
# ============================================================================


def main():
    all_entities = []

    for ontology_path in ONTOLOGY_PATHS:
        path = Path(ontology_path)
        if not path.exists():
            print(f"⚠️  Path no encontrado: {ontology_path}")
            continue

        print(f"📂 Procesando: {ontology_path}")

        for ttl_file in path.glob("*.ttl"):
            if should_exclude(ttl_file.name):
                print(f"   ⏭️  Saltando: {ttl_file.name}")
                continue

            print(f"   📄 Parseando: {ttl_file.name}")

            with open(ttl_file, "r", encoding="utf-8") as f:
                content = f.read()

            prefixes = extract_prefixes(content)
            entities = extract_entities(content, prefixes)

            # Agregar info del archivo fuente
            for e in entities:
                if not e.get("source_ontology"):
                    e["source_ontology"] = ttl_file.stem

            all_entities.extend(entities)
            print(f"      → {len(entities)} entidades encontradas")

    # Eliminar duplicados por URI
    unique = {}
    for e in all_entities:
        uri = e.get("uri")
        if uri not in unique or e.get("definition"):
            unique[uri] = e

    entities = list(unique.values())
    print(f"\n📊 Total entidades únicas con definición: {len(entities)}")

    generate_markdown(entities, OUTPUT_PATH)


if __name__ == "__main__":
    main()
