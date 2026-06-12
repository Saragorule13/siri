from tools import open_app, open_website
from router import decide_tool
from llm import ask_llm
from voice.stt import record_audio, transcribe_audio

print("🎤 Siri Voice Assistant Ready")
print("Say 'exit', 'quit', or 'bye' to stop.\n")

while True:

    input("\nPress ENTER and speak...")

    audio_file = record_audio()

    query = transcribe_audio(audio_file)

    query = query.strip().lower()

    print(f"You: {query}")

    # Empty transcription
    if not query:
        print("Siri: I didn't catch that.\n")
        continue

    # Exit commands
    if query in ["exit", "quit", "bye"]:
        print("Siri: Goodbye!")
        break

    # AI Router
    decision = decide_tool(query)

    print(f"[DEBUG] Router Decision: {decision}")

    # Open Application
    if decision.get("tool") == "open_application":

        result = open_app(decision["target"])

        print(f"Siri: {result}\n")

    # Open Website
    elif decision.get("tool") == "open_website":

        result = open_website(decision["target"])

        print(f"Siri: {result}\n")

    # Normal Chat
    else:

        response = ask_llm(query)

        print(f"Siri: {response}\n")