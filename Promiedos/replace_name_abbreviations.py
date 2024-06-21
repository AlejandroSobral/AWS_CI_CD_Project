def replace_name_abbreviations(name):
    replacements = {
        "CL": "Clausura",
        "AP": "Apertura",
        "IN": "Inicial",
        "FIN": "Final",
        "MET": "Metropolitano",
        "NAC": "Nacional",
        "CdH": "Copa de Honor",
        "CC": "Copa Campeonato",
        "AmF": "Asociación Amateur de Fútbol",
        "AAF": "Asociación Amateur de Fútbol",
        "FAF": "Federación Argentina de Fútbol",
        "LAF": "Liga Argentina de Fútbol"
    }
    for abbrev, full_name in replacements.items():
        name = name.replace(abbrev, full_name)
    
    return name