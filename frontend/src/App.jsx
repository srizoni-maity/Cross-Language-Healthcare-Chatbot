import React, {useState} from "react"; 

export default function App(){
  const [bengali, setBengali] = useState("");
  const [parsed, setParsed] = useState(null);
  const [doctorReply, setDoctorReply] = useState("");
  const [patientFacing, setPatientFacing] = useState(null);

  async function submitSymptom(){
    try{
      const res = await fetch("http://localhost:8000/parse", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({text: bengali})
      });
      const data = await res.json();
      setParsed(data);
      setPatientFacing(null);
    }catch(e){
      alert("Error connecting to backend!");
    }
  }

  async function sendDoctorReply(){
    try{
      const res = await fetch("http://localhost:8000/doctor_reply", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({doctor_reply_english: doctorReply, context_structured: parsed?.structured || {}})
      });
      const data = await res.json();
      setPatientFacing(data);
    }catch(e){
      alert("Error sending doctor reply!");
    }
  }

  return (
    <div style={{fontFamily:"Arial, sans-serif", padding:20, background:"#f5f5f5", minHeight:"100vh"}}>
      <h2 style={{color:"#2c3e50"}}>🌐 Cross-Language Healthcare Chatbot — Demo</h2>

      <div style={{marginBottom:10, background:"#fff", padding:15, borderRadius:10, boxShadow:"0 2px 6px rgba(0,0,0,0.1)"}}>
        <label style={{fontWeight:"bold"}}>Villager describes symptoms (Bengali):</label><br/>
        <textarea rows={4} cols={60} value={bengali} onChange={e=>setBengali(e.target.value)} placeholder="e.g., আমার ৩ দিন ধরে জ্বর ও কাশি আছে..." style={{padding:5, borderRadius:5, border:"1px solid #ccc"}}></textarea><br/>
        <button onClick={submitSymptom} style={{marginTop:5, padding:"5px 15px", borderRadius:5, background:"#3498db", color:"#fff", border:"none", cursor:"pointer"}}>Parse & Send to Doctor</button>
      </div>

      {parsed && (
        <div style={{marginTop:15, background:"#fff", padding:15, borderRadius:10, boxShadow:"0 2px 6px rgba(0,0,0,0.1)"}}>
          <h3 style={{color:"#16a085"}}>Structured output (for clinician)</h3>
          <pre>{JSON.stringify(parsed.structured, null, 2)}</pre>
          <h4>English hint:</h4>
          <div>{parsed.english_translation}</div>

          {parsed.severity && <div><strong>Severity:</strong> {parsed.severity}</div>}
          {parsed.red_flags && parsed.red_flags.length>0 && <div><strong>Red Flags:</strong> {parsed.red_flags.join(", ")}</div>}
          {parsed.suggested_medicines && <div><strong>Suggested Medicines:</strong> {parsed.suggested_medicines}</div>}
        </div>
      )}

      {parsed && (
        <div style={{marginTop:15, background:"#fff", padding:15, borderRadius:10, boxShadow:"0 2px 6px rgba(0,0,0,0.1)"}}>
          <label style={{fontWeight:"bold"}}>Doctor (type reply in English):</label><br/>
          <textarea rows={3} cols={60} value={doctorReply} onChange={e=>setDoctorReply(e.target.value)} placeholder="e.g., Give paracetamol and rest; advise follow-up" style={{padding:5, borderRadius:5, border:"1px solid #ccc"}}></textarea><br/>
          <button onClick={sendDoctorReply} style={{marginTop:5, padding:"5px 15px", borderRadius:5, background:"#27ae60", color:"#fff", border:"none", cursor:"pointer"}}>Translate for patient</button>
        </div>
      )}

      {patientFacing && (
        <div style={{marginTop:15, background:"#e8f8f5", padding:15, borderRadius:10, boxShadow:"0 2px 6px rgba(0,0,0,0.1)"}}>
          <h3 style={{color:"#d35400"}}>Patient-facing Bengali (simple)</h3>
          <div>{patientFacing.patient_facing_bengali}</div>
          {patientFacing.flags && patientFacing.flags.length>0 && <div><strong>Flags:</strong> {patientFacing.flags.join(", ")}</div>}
        </div>
      )}
    </div>
  );
}
