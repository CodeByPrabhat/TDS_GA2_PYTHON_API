from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from marks.json
with open("marks.json") as f:
    raw_data = json.load(f)
    marks_data = {entry["name"]: entry["marks"] for entry in raw_data}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    with open("marks.json") as f:
        data = json.load(f)

    name_to_marks = {str(entry["name"]): entry["marks"] for entry in data}
    marks = [name_to_marks.get(str(n), None) for n in name]
    marks = [m for m in marks if m is not None]  # Filter out not found

    return {"marks": marks}

@app.get("/")
def root():
    return {"message": "Use /api?name=NAME to get student marks."}
