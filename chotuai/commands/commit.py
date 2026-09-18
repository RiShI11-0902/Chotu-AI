from chotuai.utils.ollama import call_ollama

def generate_commit_message(diff):
    prompt = f'''
    You are a Git commit message generator.Analyze the following staged Git changes.Generate ONE concise commit message using Conventional Commits.Allowed types: feat: , fix: , refactor: , docs: , test: , chore:
    Return ONLY the commit message. Do not use markdown.Do not explain your answer.
    Staged changes:{diff}
    '''
    response = call_ollama(prompt)
    return response