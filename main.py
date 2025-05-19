from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from CSV into a dictionary
marks_data = {}
with open("marks.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        marks_data[row["name"]] = int(row["marks"])

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}
