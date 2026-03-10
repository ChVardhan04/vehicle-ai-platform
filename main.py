from fastapi import FastAPI, UploadFile, File
import shutil

from services.vehicle_classifier import predict_vehicle
from services.damage_detector import detect_damage
from services.intent_detector import detect_intent
from fusion import generate_service_record

app = FastAPI()

@app.post("/analyze_vehicle")

async def analyze_vehicle(image: UploadFile = File(...), text: str = ""):

    path = f"temp_{image.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    vehicle = predict_vehicle(path)

    damages = detect_damage(path)

    intent = detect_intent(text)

    result = generate_service_record(vehicle, damages, intent, {})

    return result