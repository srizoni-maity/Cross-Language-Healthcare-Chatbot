import os
from openai import OpenAI
from app.nlp import convert_bengali_digits, detect_severity, detect_red_flags

# Initialize OpenAI client from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple Bengali → English translation
def translate_to_english(text):
    mapping = {"জ্বর":"fever", "কাশি":"cough", "মাথা ব্যথা":"headache"}
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text

# Simplify English → Bengali for patient
def translate_to_bengali_simple(text, context_structured={}):
    mapping = {"fever":"জ্বর", "cough":"কাশি", "headache":"মাথা ব্যথা"}
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text

# GPT-based medicine suggestions
def suggest_medicine(structured_symptoms):
    if not structured_symptoms.get("symptoms"):
        return "No symptoms detected. Please consult a doctor."

    symptom_names = [s["name"] for s in structured_symptoms["symptoms"]]
    prompt = f"""
Patient has the following symptoms: {symptom_names}.
Suggest safe, general over-the-counter medicine advice in English (non-clinical, patient-friendly instructions).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        advice = response.choices[0].message.content
    except Exception as e:
        advice = "Could not generate medicine advice at this time."
        print("OpenAI API error:", e)

    return advice
