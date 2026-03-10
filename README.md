# Multi-Modal Vehicle Intelligence Platform

This project builds an AI system that understands vehicle information from multiple inputs.

The system combines:

- Computer Vision (vehicle and damage detection)
- Natural Language Processing (customer intent)
- Data fusion pipeline
- FastAPI inference API

Inputs
- Vehicle image
- Customer text request

Output

{
  vehicle_type: "car",
  detected_damage: ["scratch"],
  customer_intent: "insurance_claim",
  service_priority: "high"
}

Tech Stack
- Python
- FastAPI
- PyTorch
- YOLO
- Transformers

Run the API

pip install -r requirements.txt

uvicorn main:app --reload

Open

http://127.0.0.1:8000/docs