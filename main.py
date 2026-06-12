from tools import open_app, open_website
from router import decide_tool
from llm import ask_llm

print("Siri is listening...")
print("Type exit to quit.\n")

while True:

    query = input("You: ").strip().lower()

    if query in ["exit", "quit", "bye"]:
        print("Siri: Goodbye!")
        break
    
    decision = decide_tool(query)
    if decision["tool"] == "open_application":
        result = open_app(decision["target"])
        print(f"Siri: {result}\n")

    elif decision["tool"] == "open_website":
        result = open_website(decision["target"])
        print(f"Siri: {result}\n")

    else:
        response = ask_llm(query)
        print(f"Siri: {response}\n")
