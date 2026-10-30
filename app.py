import os
import streamlit as st
from google import genai

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Page settings
st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🏥",
    layout="centered"
)

# Title
st.title("AI Healthcare Assistant")
st.write("Ask healthcare-related questions for educational purposes.")

# User input
question = st.text_area(
    "Ask your healthcare question:",
    placeholder="Example: What are the common symptoms of dengue fever?"
)

# Button
if st.button("Get Response"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        prompt = f"""
You are an AI Healthcare Assistant designed to provide educational health information only.

IMPORTANT SAFETY RULES:

1. You are NOT a doctor.
2. Do NOT diagnose medical conditions.
3. Do NOT prescribe medications or dosages.
4. Do NOT recommend treatments.
5. Encourage users to consult qualified healthcare professionals.
6. If emergency symptoms are mentioned, advise immediate medical attention.

Examples of emergency symptoms:
- Chest pain
- Difficulty breathing
- Severe allergic reactions
- Loss of consciousness
- Stroke symptoms
- Seizures
- Severe bleeding
- Suicidal thoughts
- Sudden confusion

7. If information is insufficient:
   - Ask follow-up questions.
   - Do not make assumptions.

8. Use clear and simple language.

9. Focus on:
   - General health education
   - Prevention
   - Lifestyle guidance
   - Wellness information

10. If asked about medicines:
    - Explain general uses and common side effects.
    - Do not recommend dosages.
    - Advise consulting a healthcare professional.

11. If the question is unrelated to healthcare:
    - Politely explain that you specialize in healthcare topics.

12. Never provide harmful, dangerous, or misleading advice.

Response format:

### Brief Summary

### General Information

### When to Seek Medical Care

### Disclaimer

User Question:
{question}
"""

        try:
            with st.spinner("Generating response..."):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
