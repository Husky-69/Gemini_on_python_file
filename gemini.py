import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyDnLMzeYqQjH1eiyLqI7V3ZkSoMUm_q1LM")

# Set up the model
model = genai.GenerativeModel("models/gemini-2.0-flash-lite")

print("Welcome to the Gemini Chatbot!")
print("Type 'exit' to end the conversation.")

history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    history.append({"role": "user", "parts": [user_input]})
    response = model.generate_content(history)
    response_text = response.text
    history.append({"role": "model", "parts": [response_text]})
    print("Gemini: ", response_text)