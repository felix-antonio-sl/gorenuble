import re
import os

files = [
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_001_transferencia_ppr_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_011_selector_ipr_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_019_gestion_ipr_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_024_guia_idi_sni_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_025_guia_programas_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_026_guia_fril_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_027_guia_frpd_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_028_instructivo_subvencion_8_koda.yml",
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/kb_gn_029_guia_circ33_koda.yml",
]

unique_terms = set()

for fpath in files:
    try:
        if not os.path.exists(fpath):
            print(f"Warning: File not found {fpath}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                match = None
                if "Sigla:" in line:
                    match = re.search(r'Sigla:\s*"?([^"]+)"?', line)
                elif "Nombre:" in line:
                    match = re.search(r'Nombre:\s*"?([^"]+)"?', line)
                elif "Cpt:" in line:
                    match = re.search(r'Cpt:\s*"?([^"]+)"?', line)
                elif "Titulo:" in line:
                    match = re.search(r'Titulo:\s*"?([^"]+)"?', line)

                if match:
                    # Capture the group, strip whitespace, remove trailing quote if regex didn't catch it cleanly
                    term = match.group(1).strip()
                    if term.endswith('"'):
                        term = term[:-1]
                    # Specific cleanup for some common patterns in these files
                    if term.strip() and len(term) > 1:
                        unique_terms.add(term)

    except Exception as e:
        print(f"Error reading {fpath}: {e}")

filtered_terms = sorted(list(unique_terms))

output_path = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/ipr/glosario.yml"
)
with open(output_path, "w", encoding="utf-8") as f:
    for term in filtered_terms:
        # Escape quotes if present
        safe_term = term.replace('"', '\\"')
        f.write(f'- "{safe_term}"\n')

print(f"Extracted {len(filtered_terms)} terms to {output_path}")
