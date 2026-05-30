import google.generativeai as genai

from utils.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Conversation memory
conversation_history = []

def generate_response(user_input):
    print("🤖 Generating AI response...")

    # Add user message to memory
    conversation_history.append(f"User: {user_input}")

    # Create full conversation context
    full_prompt = "\n".join(conversation_history)

    # Generate AI response
    response = model.generate_content(full_prompt)

    assistant_reply = response.text

    # Store assistant response in memory
    conversation_history.append(f"Assistant: {assistant_reply}")

    print("✅ Response generated!")

    return assistant_reply