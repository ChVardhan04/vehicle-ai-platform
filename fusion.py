def generate_service_record(vehicle, damages, intent, metadata):

    priority = "low"

    if "dent" in damages or "shatter" in damages:
        priority = "high"

    if intent == "insurance_claim":
        priority = "high"

    return {

        "vehicle_type": vehicle,
        "detected_damage": damages,
        "customer_intent": intent,
        "service_priority": priority,
        "metadata": metadata
    }