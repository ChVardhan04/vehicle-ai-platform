def detect_intent(text):

    text = text.lower()

    if "insurance" in text:
        return "insurance_claim"

    if "damage" in text:
        return "damage_report"

    if "service" in text:
        return "service_request"

    return "general_query"