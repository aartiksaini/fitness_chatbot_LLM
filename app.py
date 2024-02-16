import requests
import streamlit as st
import cohere
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# --- Configuration ---
EDAMAM_NUTRITION_URL = "https://api.edamam.com/api/nutrition-data"

# Load API keys from Streamlit Secrets
edamam_app_id = os.environ["EDAMAM_APP_ID"]
edamam_app_key = os.environ["EDAMAM_APP_KEY"]
cohere_api_key = os.environ["COHERE_API_KEY"]

# Initialize the Cohere Client
co = cohere.Client(cohere_api_key)

def get_nutrition_fact(food):
    params = {
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
        "ingr": f"1 {food}"  # Added quantity 
    }
    response = requests.get(EDAMAM_NUTRITION_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        calories = data['calories']
        return f"{food} has approximately {calories} calories."
    else:
        return "Nutrition data unavailable. Try a different food or 'calories in 1 apple'"  # Improved Error Handling


def process_query(query):
    if "nutrition" in query or "calories" in query:
        food = query.split(" ", 1)[1]  # Simple food item extraction
        return get_nutrition_fact(food)
    else:  
        # Construct fitness-focused prompt for Cohere 
        response = co.generate( 
            model='command-nightly',  
            prompt=f"You are a fitness expert. Answer this user's query in a few short helpful sentences: {query}", 
            temperature=0.8, 
            stop_sequences=["--"])
        return response.generations[0].text

# --- Streamlit App ---


# chat_history = []  

# --- Streamlit App ---
st.title("Fitness and Nutrition Chatbot")

# for message in chat_history:
#     if "User:" in message:
#         st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)
#     else:  # Assumes it's the chatbot
#         st.markdown(f"<div class='chatbot-message'>{message}</div>", unsafe_allow_html=True)

user_input = st.text_input("Ask me about fitness or nutrition:")

if st.button("Submit"): 
    chatbot_response = process_query(user_input)
    chat_history.append("User: " + user_input)
    chat_history.append("Chatbot: " + chatbot_response)
    st.write("Chatbot:", chatbot_response) 
