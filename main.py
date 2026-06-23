from fastapi import FastAPI
from intent_agent import extract_intent
from design_agent import generate_design
from schema_agent import generate_schema
from validator import validate
from repair import repair

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI App Compiler Running"}

@app.get("/generate")
def generate(prompt: str):

    intent = extract_intent(prompt)

    design = generate_design(intent)

    schema = generate_schema(design)

    validate(schema)

    final_schema = repair(schema)

    return {
        "intent": intent,
        "design": design,
        "schema": final_schema
    }