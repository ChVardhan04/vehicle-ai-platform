import random

damage_types = [
    "dent",
    "scratch",
    "no_damage"
]

def detect_damage(image_path):

    damage = random.choice(damage_types)

    if damage == "no_damage":
        return []

    return [damage]