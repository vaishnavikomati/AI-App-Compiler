def generate_schema(design):

    tables = []

    for entity in design["entities"]:
        tables.append(entity.lower() + "s")

    return {
        "tables": tables
    }