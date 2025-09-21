#This file help you to implement ai in your chatbot

import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyD27MhgmMPpNgyeMS_REs4M1kLsZhAEMh4")


var1=("aur bataop kaisy ho")

# Choose the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the prompt
prompt = """You are a person named Aryan who speaks Hindi as well as English. 
He is from India and is a coder. You analyze chat history and respond like Aryan.

{var1}
"""

# Generate content
response = model.generate_content(prompt)

# Print the response
print(response.text)
