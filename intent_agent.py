def extract_intent(prompt):
    return {
        "app_name": prompt,
        "roles": ["Admin", "User"]
    }