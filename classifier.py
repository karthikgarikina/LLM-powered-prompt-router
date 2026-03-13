import json
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

CLASSIFIER_PROMPT = """
Classify the user's intent into one of these categories:

code
data
writing
career
unclear

Return JSON in this format:

{
 "intent": "code",
 "confidence": 0.92
}
"""


def classify_intent(message: str):
    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        content = response.choices[0].message.content
        parsed = json.loads(content)

        return {
            "intent": parsed.get("intent", "unclear"),
            "confidence": float(parsed.get("confidence", 0.0))
        }

    except Exception:
        return {
            "intent": "unclear",
            "confidence": 0.0
        }
