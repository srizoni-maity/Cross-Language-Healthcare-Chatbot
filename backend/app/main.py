from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

from app.nlp import parse_bengali_symptoms
from app.translator import translate_to_english, translate_to_bengali_simple, suggest_medicine

app = FastAPI(title="Cross-Language Healthcare Chatbot - Prototype")

# -------------------- Request & Response Schemas --------------------
class ParseRequest(BaseModel):
    text: str

class ParseResponse(BaseModel):
    original_text: str
    structured: dict
    english_translation: str
    suggested_medicines: str

class DoctorReplyRequest(BaseModel):
    doctor_reply_english: str
    context_structured: Optional[dict] = None

class DoctorReplyResponse(BaseModel):
    original_doctor_reply: str
    patient_facing_bengali: str
    flags: Optional[List[str]] = None

# -------------------- Endpoints --------------------
@app.post("/parse", response_model=ParseResponse)
def parse(request: ParseRequest):
    english = translate_to_english(request.text)
    structured = parse_bengali_symptoms(request.text, english)

    suggested_medicines = suggest_medicine(structured)

    return ParseResponse(
        original_text=request.text,
        structured=structured,
        english_translation=english,
        suggested_medicines=suggested_medicines
    )

@app.post("/doctor_reply", response_model=DoctorReplyResponse)
def doctor_reply(req: DoctorReplyRequest):
    bengali = translate_to_bengali_simple(req.doctor_reply_english, req.context_structured or {})

    flags = []
    if "emergency" in req.doctor_reply_english.lower() or "go to hospital" in req.doctor_reply_english.lower():
        flags.append("urgent_care_recommended")

    return DoctorReplyResponse(
        original_doctor_reply=req.doctor_reply_english,
        patient_facing_bengali=bengali,
        flags=flags
    )

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, restrict to frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
