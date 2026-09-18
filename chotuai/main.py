import sys
from rich.console import Console
from rich.markdown import Markdown

from chotuai.utils.get_diff import get_diff
from chotuai.commands.commit import generate_commit_message
from chotuai.commands.review_code import generate_review
from chotuai.commands.setup import setup_ollama
console = Console()

def commit_message():
    diff = get_diff()

    if not diff:
        print("No staged changes found.")
        return

    print("Generating commit message...")

    message = generate_commit_message(diff)

    print("\nSuggested commit message:")
    print(message)

def review_code(filepath,isFile):
    if isFile:
        with open(filepath,"r", encoding="utf-8") as file:
            code = file.read()

        print("Generating Review...")
        review = generate_review(code)
        console.print(Markdown(review))
    else:
        print("Please paste your code and then write end")
        
        lines = []
        
        while True:
                line = input()
        
                if line == 'end' or line == 'END':
                    break
                lines.append(line)
        
                code_snippet = "\n".join(lines)
        
        if not code_snippet.strip():
                print("No code provided.")
                return
        
        print("Generating Review...")
            
        review = generate_review(code_snippet)
        
        print("\nCode Review:")
        console.print(Markdown(review))

def main():
    if len(sys.argv) < 2:
        print('Please Provide a command')
        sys.exit(1)

    command = sys.argv[1]

    if command == "commit-message":
        commit_message()
    elif command == "review-file":
        filepath = sys.argv[2]
        if filepath:
            review_code(filepath,True)
        else:
            print("Please provide filepath")
    elif command == "review-snippet":
        review_code("", False)
    elif command == "setup":
        print("Welcome to ChotuAI!")
        setup_ollama()
    else:
        print("Unknown  command")

if __name__ == "__main__":
    main()





