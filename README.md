# Cross-Language Healthcare Chatbot (Prototype)

**Core idea:** A global chatbot that translates symptoms described in local languages (example: Bengali) into structured medical terms in English for clinicians, and converts clinician replies back into simple local-language explanations for the patient.

This repository is a high-level, runnable prototype. It is *NOT* a medical device. Do not use in production without clinical validation and legal review.

## What's included
- `backend/` : FastAPI backend with endpoints:
  - `/parse` : parse Bengali free-text symptoms → structured JSON (rule-based prototype)
  - `/doctor_reply` : accepts a doctor's English reply and produces a simple Bengali translation
  - `/translate` : placeholder translator interface showing where an ML/translation API would be used
- `frontend/` : Minimal React app (single-file) to demo the flow
- `sample_data/` : Example Bengali symptom descriptions and sample interaction
- `Dockerfile` and `docker-compose.yml` : quick dev/devops scaffolding
- `README.md` : this file with usage and safety notes

## How to run (local dev)
1. Backend (Python):
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
2. Frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```
3. Or use Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Design notes (high-level)
- **Input (villager)**: free-text in Bengali.
- **Step 1 (NLP/transformation)**: convert to structured JSON (symptoms, onset, duration, severity, red flags). Prototype uses rule-based extraction and a small bilingual lexicon.
- **Step 2 (Clinician view)**: structured JSON + original text is shown to doctor. Doctor types a reply in medical English.
- **Step 3 (Backtranslation & simplification)**: reply is simplified and translated into Bengali in simple words for the patient.
- **Extensibility**: replace translation modules with cloud translation APIs (e.g. Google Translate) or fine-tuned LLM for clinical mapping; replace rule-based parser with an entity extraction model.

## Safety, ethics & legal
- This is a prototype. Medical correctness is not guaranteed.
- Always surface a "seek immediate care" warning for red flags (danger signs).
- Log and audit translations / clinician confirmations in production.
- Add HIPAA/GDPR compliance, secure transport (HTTPS), auth, consent before deployment.

## Files
See the project tree for details.

---
