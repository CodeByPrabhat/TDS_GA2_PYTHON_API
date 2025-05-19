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
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
