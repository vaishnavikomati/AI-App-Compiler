def generate_schema(design):

    return {
        "tables": [
            "users",
            "tasks"
        ],

        "api_routes": [
            "/users",
            "/tasks"
        ]
    }