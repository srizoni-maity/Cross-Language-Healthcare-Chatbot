#!/usr/bin/env python3
import requests, json, sys
BASE="http://localhost:8000"
s = "আমার ৩ দিন ধরে জ্বর ও কাশি আছে, মাঝে মাঝে শ্বাস নিতে কষ্ট হয়।"
r = requests.post(BASE+"/parse", json={"text":s}).json()
print("Parsed:", json.dumps(r, ensure_ascii=False, indent=2))
reply = "Give paracetamol for fever, advise rest, if shortness of breath worsens seek emergency care."
r2 = requests.post(BASE+"/doctor_reply", json={"doctor_reply_english": reply, "context_structured": r['structured']}).json()
print("Patient-facing:", json.dumps(r2, ensure_ascii=False, indent=2))
