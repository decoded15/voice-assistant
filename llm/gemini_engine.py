import google.generativeai as genai

from utils.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(user_input):
    print("🤖 Generating AI response...")

    response = model.generate_content(user_input)

    print("✅ Response generated!")

    return response.text