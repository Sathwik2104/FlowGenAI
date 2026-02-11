import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# REPLACE WITH YOUR REAL KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_gemini_flow(topic):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # We ask specifically for Mermaid.js syntax
    prompt = f"""
    You are a flowchart generator. Create a mermaid.js flowchart for: {topic}.
    
    Strict Rules:
    1. Start with 'graph TD'
    2. Use square brackets [] for process steps.
    3. Use diamond brackets {{}} for decisions.
    4. Do not include markdown ticks (```mermaid). Just the raw code.
    5. Keep text inside nodes short (max 5 words).
    
    Example output format:
    graph TD
    A[Start] --> B[Step 1]
    B --> C{{Decision?}}
    C -- Yes --> D[Result A]
    C -- No --> E[Result B]
    """
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        # Clean up if the AI accidentally adds markdown
        clean_text = response.text.replace("```mermaid", "").replace("```", "").strip()
        return clean_text
    except Exception as e:
        return f"graph TD\nA[Error] --> B[{str(e)}]"