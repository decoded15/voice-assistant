import google.generativeai as genai

from utils.config import GEMINI_API_KEY
from llm.personality import ASSISTANT_PERSONALITY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Conversation memory
conversation_history = []

def generate_response(user_input):
    print("🤖 Generating AI response...")

    # Store user message
    conversation_history.append(f"User: {user_input}")

    # Build conversation context
    conversation_context = "\n".join(conversation_history)

    # Final prompt
    full_prompt = f"""
        {ASSISTANT_PERSONALITY}

        Conversation so far:
        {conversation_context}

        Assistant:
        """

    # Generate response
    response = model.generate_content(full_prompt)

    assistant_reply = response.text

    # Store assistant reply
    conversation_history.append(f"Assistant: {assistant_reply}")

    print("✅ Response generated!")

    return assistant_reply