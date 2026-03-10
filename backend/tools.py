from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def log_interaction(message):

    # normally save to database

    return f"Interaction logged: {message}"


def edit_interaction(message):

    return "Interaction updated successfully"


def get_doctor_history(message):

    return "Doctor history: Dr Rao discussed diabetes medicine previously"


def summarize_interaction(message):

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this doctor interaction: {message}"
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Summary could not be generated: {str(e)}"


def suggest_next_action(message):

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Suggest next sales action: {message}"
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Suggestion could not be generated: {str(e)}"