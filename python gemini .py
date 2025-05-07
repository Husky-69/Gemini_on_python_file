import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyDnLMzeYqQjH1eiyLqI7V3ZkSoMUm_q1LM")

# List available models
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}, Description: {model.description}")

# Exit after listing models
exit()