from fastapi import FastAPI, UploadFile, File
from formatter import format_notes, format_table

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/notes")
async def notes(file: UploadFile = File(...)):
    content = await file.read()
    return {"result": format_notes(content.decode(errors="ignore"))}
