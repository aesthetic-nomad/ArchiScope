from fastapi import APIRouter
from app.utils.classifier import classify_style

router = APIRouter()

@router.get("/classify/{photo_id}")
async def classify(photo_id: str):
    style = classify_style(photo_id)
    return {"photo_id": photo_id, "style": style}
