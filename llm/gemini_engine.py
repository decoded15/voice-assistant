import google.generativeai as genai
import time

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
    response_stream = model.generate_content(
        full_prompt,
        stream=True
    )

    assistant_reply = ""

    print("🤖 Assistant: ", end="", flush=True)

    for chunk in response_stream:
        if chunk.text:
            for char in chunk.text:
                print(char, end="", flush=True)
                time.sleep(0.02)

            assistant_reply += chunk.text

    print("\n")

    # Save assistant reply into memory
    conversation_history.append(f"Assistant: {assistant_reply}")

    return assistant_reply