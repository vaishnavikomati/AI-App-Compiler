def generate_design(intent):

    app = intent["app_name"].lower()

    if "library" in app:
        entities = ["Book", "Student", "Librarian"]

    elif "hospital" in app:
        entities = ["Doctor", "Patient", "Appointment"]

    elif "ecommerce" in app:
        entities = ["Product", "Customer", "Order"]

    else:
        entities = ["User", "Task"]

    return {"entities": entities}