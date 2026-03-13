from groq import Groq
from prompts import PROMPTS
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def route_and_respond(message: str, intent_data: dict):

    intent = intent_data["intent"]

    if intent == "unclear":
        return (
            "I'm not sure what kind of help you're looking for.\n\n"
            "Are you asking about:\n"
            "- coding\n"
            "- data analysis\n"
            "- writing improvement\n"
            "- career advice?"
        )

    system_prompt = PROMPTS.get(intent)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
