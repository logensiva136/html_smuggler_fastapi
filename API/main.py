from pathlib import Path
from tempfile import TemporaryDirectory
from uvicorn import run 
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/")
def generate(data:UploadFile):
    with TemporaryDirectory() as tmpdirname:
        path_ = Path(tmpdirname) / data.filename
        with open(path_, "wb") as buffer:
            buffer.write(data.file.read())
        return {"filename": data.filename, "filepath": tmpdirname+"/"+data.filename}



if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8765, reload=True)