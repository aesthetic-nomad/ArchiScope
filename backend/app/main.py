from fastapi import FastAPI
from app.routes import photos, styles

app = FastAPI()

app.include_router(photos.router, prefix="/photos", tags=["Photos"])
app.include_router(styles.router, prefix="/styles", tags=["Styles"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ArchiScope API"}
