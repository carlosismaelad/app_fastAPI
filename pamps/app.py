from fastapi import FastAPI

app = FastAPI(
    title="Pamps",
    version="0.1.0",
    description="Pamps is a posting app",
)

@app.get("/")
async def index():
    return {"message": "API ok!"}