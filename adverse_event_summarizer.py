from dotenv import load_dotenv
import os
import google.generativeai as genai

# 1. Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. Define the model (free, fast)
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. System prompt – role definition
system_prompt = """
You are a clinical pharmacist. Extract adverse drug events from clinical notes.
Return ONLY a JSON object with the following fields:
- "event": the adverse event description
- "severity": one of "mild", "moderate", "severe"
- "suspect_drug": the drug most likely responsible
If no adverse event is present, return {"event": "none", "severity": "none", "suspect_drug": "none"}.
"""

# 4. Few-shot example (teaches the output format)
example_input = """
Patient presented with severe nausea and vomiting 2 days after starting metformin 500mg.
No other medications changed. Symptoms resolved after stopping metformin.
"""
example_output = """
{"event": "severe nausea and vomiting", "severity": "severe", "suspect_drug": "metformin"}
"""

# 5. The real clinical note to analyze
clinical_note = """
Patient started on lisinopril 10mg three days ago. Today reports a persistent dry cough
that began yesterday. No fever, no shortness of breath. Cough is irritating but not severe.
"""

# 6. Build the full prompt
full_prompt = f"""
{system_prompt}

Example input:
{example_input}

Example output:
{example_output}

Now analyze this clinical note and return ONLY the JSON:
{clinical_note}
"""

# 7. Call Gemini and print the result
response = model.generate_content(full_prompt)
print("=== ADVERSE EVENT SUMMARY ===")
print(response.text)
