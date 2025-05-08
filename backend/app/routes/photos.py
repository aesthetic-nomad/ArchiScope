from fastapi import APIRouter, UploadFile, File
from app.models.photo import Photo
import shutil
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"data/sample_images/{file_id}_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "id": file_id}
