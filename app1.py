import streamlit as st
import google.generativeai as ai

# Load API key from Streamlit Secrets
key = st.secrets["api"]["key"]

# Configure AI model
ai.configure(api_key=key)

# System instructions for the AI Code Reviewer
sys_prompt = """
You are an advanced AI Code Reviewer for Python.
Your job is to analyze submitted Python code, identify potential bugs, errors, or areas of improvement,
and suggest optimized and corrected versions of the code.
Ensure your suggestions follow best coding practices, improve efficiency, and enhance readability.
If the code is already optimal, acknowledge it but provide possible enhancements if applicable.
If a student asks something outside python code, politely decline.
"""

# Initialize AI Model
model = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

# Streamlit UI
st.title("AI Python Code Reviewer")
st.write("Submit your Python code below for analysis and improvements.")

# Text area for code input
user_code = st.text_area("Paste your Python code here:",  placeholder="Write or paste your Python code...")

# Button to generate review
if st.button("Review Code"):
    if user_code.strip():  
        response = model.generate_content(f"Analyze the following Python code and suggest improvements or fixes:\n\n{user_code}")
        st.subheader("Code Review & Suggestions:")
        st.write(response.text)  # Display AI's response
    else:
        st.warning("Please enter Python code before clicking the button.")
