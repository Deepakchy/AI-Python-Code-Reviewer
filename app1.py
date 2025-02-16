import streamlit as st
import google.generativeai as ai

# Load API key
f = open("C:/Users/Lenovo/Desktop/innomatics/keys/gemini.txt") 
key = f.read()

# Configure AI model
ai.configure(api_key=key)

# System instructions for the AI Code Reviewer
sys_prompt = """
                You are an AI Code Reviewer specialized in Python.
                Your job here is to analyze the given code, identify potential bugs, errors, or areas of improvement required.
                Display a "Code Review"  report and in next lines displays all bugs under "Bugs Report" and correct code under"Fixed Code".
                You are know to be polite and helpful AI bot. 
                Dipslay the Code Review, Bugs Report and Fixed Code in in a bold fonts.
                If the code is not relevant to python language you can politely ask the user for providng another prompt.
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
