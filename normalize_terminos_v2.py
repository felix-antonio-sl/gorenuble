import re

mappings = {
    "COMV": "SOC",
    "DIG": "TDE",
    "DOC": "SYS",
    "EXT": "FIN",
    "JUEZ": "NORM",
    "OIRS": "SOC",
    "OPS": "SYS",
    "ORM": "FIN",
    "RG": "FIN",
    "SAL": "SEG",
}


def normalize_term(term):
    for old, new in mappings.items():
        if term.startswith(f"ENT-{old}-"):
            return term.replace(f"ENT-{old}-", f"ENT-{new}-")
    return term


md_path = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/terminos.md"
)

with open(md_path, "r") as f:
    terms = [line.strip() for line in f if line.strip()]

normalized_terms = sorted(list(set(normalize_term(t) for t in terms)))

with open(md_path, "w") as f:
    for t in normalized_terms:
        f.write(f"{t}\n")

print(f"Refactor complete. Total terms: {len(normalized_terms)}")
