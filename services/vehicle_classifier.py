import random

vehicle_types = [
    "car",
    "bike",
    "truck",
    "suv"
]

def predict_vehicle(image_path):

    return random.choice(vehicle_types)