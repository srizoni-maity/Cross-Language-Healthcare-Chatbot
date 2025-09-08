# app/nlp.py
import re

bn_digits = "০১২৩৪৫৬৭৮৯"
ar_digits = "0123456789"

severity_keywords = {
    "হালকা": "mild", "মৃদু": "mild",
    "মাঝারি": "moderate", "তীব্র": "severe", "ভয়াবহ": "severe"
}

red_flag_keywords = [
    "শ্বাস নিতে সমস্যা", "রক্ত", "চোখের সমস্যা", "হঠাৎ জ্বর", "গুরুতর ব্যথা"
]

symptom_mapping = {
    "জ্বর": "fever",
    "কাশি": "cough",
    "মাথা ব্যথা": "headache",
    "ঠান্ডা": "cold",
    "গ্যাস্ট্রিক": "stomach pain"
}

def convert_bengali_digits(text: str) -> str:
    for bn, ar in zip(bn_digits, ar_digits):
        text = text.replace(bn, ar)
    return text

def detect_severity(text: str):
    for k, v in severity_keywords.items():
        if k in text:
            return v
    return None

def detect_red_flags(text: str):
    return [flag for flag in red_flag_keywords if flag in text]

def parse_bengali_symptoms(text: str, english_text: str = None):
    structured = {"symptoms": [], "duration": None, "severity": None, "red_flags": [], "notes": "This is a prototype, not a clinical diagnosis."}

    # Detect symptoms
    for bn_word, en_word in symptom_mapping.items():
        if bn_word in text:
            structured["symptoms"].append({"name": en_word, "source_word": bn_word})

    # Detect duration (e.g., "৩ দিন ধরে" → "3 days")
    match = re.search(r'(\d+|[০-৯]+)\s*দিন', text)
    if match:
        days = convert_bengali_digits(match.group(1))
        structured["duration"] = f"{days} days"

    # Detect severity
    structured["severity"] = detect_severity(text)

    # Detect red flags
    structured["red_flags"] = detect_red_flags(text)

    return structured
