#  Bhasha-Arogya: Cross-Language Health Bridge 🩺

Breaking language barriers in healthcare, one symptom at a time.

https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi

https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB

https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white



🌟 The Problem & Our Solution

Millions are left behind in healthcare due to language barriers. A patient describing symptoms in their native Bengali often gets lost in translation before reaching a doctor.

Bhasha-Arogya (Language-Health) is an AI-powered prototype designed to be that crucial bridge. It captures nuanced, village-level Bengali symptom descriptions and translates them into structured clinical data for doctors, ensuring nothing gets lost.

⚠ Critical Disclaimer: This is a prototype for demonstration and research purposes only. It is NOT a certified medical device and should NEVER be used as a substitute for professional diagnosis, advice, or treatment.


🚀 Key Features

Feature	Description	Impact :

🧠 Intelligent Symptom Parsing	NLP-powered extraction of symptoms, severity, duration, and potential red flags from colloquial Bengali.	Turns unstructured patient language into actionable, structured data.

🚨 Red Flag Detection	Automatically highlights urgent warning signs (e.g., "shosh hoye jacche" - severe dehydration) for immediate attention.	Prioritizes critical cases and alerts clinicians.

💊 AI-Powered OTC Suggestions	Leverages OpenAI GPT to generate safe, general-purpose over-the-counter medicine advice. Clearly labels it as non-prescriptive.	Provides educational context for common, minor ailments.

🔄 Doctor-Patient Translation	Converts complex English doctor instructions back into simple, understandable Bengali for the patient.	Closes the communication loop and improves health literacy.


## Tech Stack
Backend API: Python + FastAPI (High-performance, async-ready)

Frontend UI: React (with TypeScript for type safety)

AI & NLP: OpenAI GPT API + Custom Bengali regex/lexicon mappers

Authentication: (Optional) JWT / OAuth2


⚡ Quick Start :

Prerequisites

Python 3.9+

Node.js & npm

An OpenAI API key


1. Clone & Setup :
   git clone https://github.com/<your-username>/cross-language-healthbot.git
   
   cd cross-language-healthbot
   
2. Backend Setup :
   
   cd backend
   
   pip install -r requirements.txt
   
   ### Set your API Key (Unix/macOS)
   
   export OPENAI_API_KEY="your_key_here"
   
   #### For Windows (Command Prompt)
   
   setx OPENAI_API_KEY "your_key_here"
   
   #### Start the server
   
    uvicorn app.main:app --reload --port 8000
   
API docs will be live at: http://localhost:8000/docs


3. Frontend Setup :
   
   cd ../frontend
   
   npm install
   
   npm start
   
The app will be live at: http://localhost:3000



📖 How It Works: The User Journey

1. Patient Input: A user describes their symptoms in natural Bengali:
   "আমার পেটে খুব ব্যথা, বমি বমি লাগছে, এবং জ্বর হয়েছে গতকাল থেকে।" 

2. Structuring & Analysis: Our backend parses this into:
{

  "symptoms": ["abdominal pain", "nausea", "fever"],
  
  "severity": "severe",
  
  "duration": "1 day",
  
  "red_flags": []
  
}

3. AI Suggestion: GPT suggests general OTC advice (e.g., hydration, rest, common antacids) with clear disclaimers.
   
4. Doctor's Turn: A doctor reviews the structured data, makes a diagnosis, and types advice in English.
   
5. Closing the Loop: The doctor's advice is translated back into simple Bengali for the patient to understand.

   

🧪 Example API Flow :

Endpoint: POST /api/parse-symptoms

Request (Bengali Text): 

{
  "text": "মাথা ব্যাথা এবং সারা শরীরে জ্বর আছে।"
  
}

Response (Structured JSON):

{
  "structured_data": {
  
    "symptoms": ["headache", "fever"],
    
    "severity": "mild",
    
    "duration": "unknown",
    
    "red_flags": []
    
  },
  
  "ai_advice": "For general headache and fever, rest and hydration are recommended. Over-the-counter pain relievers like paracetamol may help. Consult a doctor if symptoms worsen.",
  
  "translated_advice": "মাথাব্যথা এবং জ্বরের জন্য বিশ্রাম এবং জলখাবার সুপারিশ করা হয়। প্যারাসিটামলের মতো ওভার-দ্য-কাউন্টার ব্যথানাশক সাহায্য করতে পারে। লক্ষণগুলি খারাপ হলে একজন ডাক্তারের সাথে পরামর্শ করুন।"
  
}


📂 Project Structure :
cross-language-healthbot/
├── 📁 backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app root
│   │   ├── models.py        # Pydantic models
│   │   ├── nlpparser.py     # Core Bengali NLP logic
│   │   └── ai_helper.py     # OpenAI GPT integration
│   ├── requirements.txt
│   └── README.md
└── 📁 frontend/
    ├── src/
    │   ├── components/      # React components
    │   └── App.tsx
    ├── package.json
    └── README.md

🤝 Contributing

We welcome contributions! Please feel free to submit issues, fork the repository, and create pull requests. Let's make healthcare more accessible together.

1. Fork the Project
   
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
   
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
   
4. Push to the Branch (git push origin feature/AmazingFeature)
   
5. Open a Pull Request
   

**📜 License

Distributed under the MIT License. See LICENSE file for more information.


👨‍💻 Author

Srizoni Maity

Baishakhi Sing

GitHub: [https://github.com/srizoni-maity]

LinkedIn: [https://www.linkedin.com/in/srizoni-maity-012235356]**


If this project inspires you, give it a ⭐!

