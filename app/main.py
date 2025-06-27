from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from pathlib import Path
import json
from app.middleware import hello_middleware, middleware_middleware, py_middleware

app = FastAPI()
DATA_FILE = Path("data.json")

if not DATA_FILE.exists():
    DATA_FILE.write_text('{"message": "Hello World, Py!"}')

app.middleware("http")(middleware_middleware) # Вот тут проблема с порядком
app.middleware("http")(py_middleware) # Вот тут проблема с порядком
app.middleware("http")(hello_middleware)

@app.get("/")
def get_phrase():
    return {}

@app.get("/hello")
def read_hello():
    return json.loads(DATA_FILE.read_text())

@app.post("/update")
async def update_message(new_msg: str = Body(..., embed=True)):
    DATA_FILE.write_text(json.dumps({"message": new_msg}))
    return {"status": "updated", "message": new_msg}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)