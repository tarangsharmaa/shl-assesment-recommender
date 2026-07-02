from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SHL Assessment Recommendation API"
)

app.include_router(router)

@app.get("/health")
def health():
    return{
        "status":"healthy"
    }