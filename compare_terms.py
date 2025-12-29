import re


def get_terms_from_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        terms = re.findall(r"(ENT-[A-Z0-9-]+)", content)
        return set(terms)


md_file = (
    "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/terminos.md"
)
yml_file = "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/kb_gn_014_glosario_gore_nuble_koda.yml"

md_terms = get_terms_from_file(md_file)
yml_terms = get_terms_from_file(yml_file)

missing = sorted(list(md_terms - yml_terms))

with open("/Users/felixsanhueza/Developer/gorenuble/missing_all.txt", "w") as f:
    for t in missing:
        f.write(f"{t}\n")

print(f"Written {len(missing)} missing terms to missing_all.txt")
