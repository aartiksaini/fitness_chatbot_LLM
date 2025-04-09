import pandas as pd
import cohere
import os
from dotenv import load_dotenv
import streamlit as st

# --- Load Environment Variables ---
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

if cohere_api_key is None:
    st.error("COHERE_API_KEY not found. Please check your .env file.")
    st.stop()

co = cohere.Client(cohere_api_key)

# --- Load Dataset ---
def load_exercise_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

exercise_data = load_exercise_data('megaGymDataset.csv')

# --- Gather User Preferences ---
def gather_user_preferences():
    goal = st.selectbox("What's your main fitness goal?",
                        ["Weight Loss", "Build Muscle", "Endurance", "General Fitness"])
    experience = st.radio("What's your experience level?",
                          ["Beginner", "Intermediate", "Advanced"])
    restrictions = st.checkbox("Any injuries or limitations?")
    
    return {
        "goal": goal,
        "experience": experience,
        "restrictions": restrictions
    }

# --- Process User Query ---
def process_query(query, exercise_data, user_preferences=None):
    if user_preferences is None:
        user_preferences = gather_user_preferences()

    # Craft prompt using helper
    prompt = craft_fitness_prompt(query, exercise_data, user_preferences)

    # Use chat API (updated from generate)
    response = co.chat(
        model='command-nightly',
        message=prompt
    )
    return response.text

# --- Helper Function to Craft Prompt ---
def craft_fitness_prompt(query, data, prefs):
    goal = prefs["goal"]
    experience = prefs["experience"]
    restrictions = "Yes" if prefs["restrictions"] else "No"

    prompt = (
        f"You are a certified personal trainer helping a client with the following goals:\n"
        f"- Goal: {goal}\n"
        f"- Experience Level: {experience}\n"
        f"- Injuries/Limitations: {restrictions}\n\n"
        f"The client asked: \"{query}\"\n"
        f"Please provide a helpful and specific answer."
    )
    return prompt

# --- Streamlit UI ---
st.title("🏋️ Fitness Knowledge Bot")

# Collect user preferences
user_preferences = gather_user_preferences()

# Text input for user query
user_input = st.text_input("Ask me about workouts or fitness...")

# Submit button
if st.button("Submit") and user_input:
    chatbot_response = process_query(user_input, exercise_data, user_preferences)
    st.markdown("**Chatbot:**")
    st.write(chatbot_response)
