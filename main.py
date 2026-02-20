from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from typing import List
import shutil, os, uuid

from ocr import extract_text
from formatter import format_notes, format_table
from detector import is_table

app = FastAPI()

def save_temp(file: UploadFile):
    name = f"temp_{uuid.uuid4().hex}.png"
    with open(name, "wb") as buf:
        shutil.copyfileobj(file.file, buf)
    return name

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/auto")
async def auto(files: List[UploadFile] = File(...)):
    combined = []
    for f in files:
        path = save_temp(f)
        combined.append(extract_text(path))
        os.remove(path)

    text = "\n".join(combined)

    if is_table(text):
        return {"output": format_table(text)}
    else:
        return {"output": format_notes(text)}