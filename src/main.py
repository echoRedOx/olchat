import ollama
import sys


def local_chat(model: str):
    while True:
        request =  input("\nUser >> ")

        if request == 'exit' or request == 'quit':   # Check if the user wants to exit
            print("Exiting chat...\n\n")
            break

        messages = [
            {
                'role': 'user',
                'content': request,   
            }
        ]

        stream = ollama.chat(model=model, messages=messages, stream=True) 
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

def main():
    model = sys.argv[1]
    local_chat(model=model)


if __name__ == "__main__":
    main()
