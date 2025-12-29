import re


def rebuild_hierarchy():
    filepath = "/Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/gestion/kb_gn_014_glosario_gore_nuble_koda.yml"
    with open(filepath, "r") as f:
        content = f.read()

    # Find all definitions: ENT-DOMAIN-NAME: "definition"
    defs = re.findall(r'(ENT-([A-Z0-9]+)-[A-Z0-9-]+): "(.+)"', content)

    # Organize by domain
    domains = {}
    for full_id, dom_prefix, definition in defs:
        # Normalize prefixes that might have slipped through
        final_dom = dom_prefix
        if dom_prefix == "DIG":
            final_dom = "TDE"
        elif dom_prefix == "DOC":
            final_dom = "SYS"
        elif dom_prefix == "OPS":
            final_dom = "SYS"
        elif dom_prefix == "EXT":
            final_dom = "FIN"
        elif dom_prefix == "JUEZ":
            final_dom = "NORM"
        elif dom_prefix == "OIRS":
            final_dom = "SOC"
        elif dom_prefix == "ORM":
            final_dom = "FIN"
        elif dom_prefix == "RG":
            final_dom = "FIN"
        elif dom_prefix == "SAL":
            final_dom = "SEG"
        elif dom_prefix == "COMV":
            final_dom = "SOC"

        final_id = full_id.replace(f"ENT-{dom_prefix}-", f"ENT-{final_dom}-")

        if final_dom not in domains:
            domains[final_dom] = {}
        domains[final_dom][final_id] = definition

    # Generate new content
    new_content = [
        "# KODA Artifact: Glosario Unificado GORE_OS",
        "# Canon terminológico con definiciones sintéticas y precisas",
        "# ID: GN-GLOSARIO-01",
        "---",
        "_manifest:",
        '  created_at: "2025-12-25"',
        '  version: "1.3.0"',
        "",
        "Glosario:",
    ]

    for dom in sorted(domains.keys()):
        new_content.append(f"  {dom}:")
        for term_id in sorted(domains[dom].keys()):
            new_content.append(f'    {term_id}: "{domains[dom][term_id]}"')
        new_content.append("")

    with open(filepath, "w") as f:
        f.write("\n".join(new_content))

    print(f"Rebuilt YAML with {len(defs)} terms organized by domain.")


if __name__ == "__main__":
    rebuild_hierarchy()
