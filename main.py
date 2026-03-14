from classifier import classify_intent
from router import route_and_respond
from logger import log_request
import signal
import sys


def graceful_shutdown(signum, frame):
    print("\nShutting down AI Prompt Router...")
    sys.exit(0)


signal.signal(signal.SIGINT, graceful_shutdown)
signal.signal(signal.SIGTERM, graceful_shutdown)


def main():

    print("AI Prompt Router")
    print("Type 'exit' to quit\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            break

        intent_data = classify_intent(user_message)

        print(f"\nIntent: {intent_data['intent']}")
        print(f"Confidence: {intent_data['confidence']}\n")

        response = route_and_respond(user_message, intent_data)

        print(response)
        print("\n" + "-" * 50 + "\n")

        log_request(intent_data, user_message, response)


if __name__ == "__main__":
    main()
