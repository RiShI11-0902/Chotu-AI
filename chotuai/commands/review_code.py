from chotuai.utils.ollama import call_ollama
def generate_review(code):

    prompt = f"""
    You are a code reviewer.
    
    Review the following code.
    
    Return the review using EXACTLY this structure:
    
    ## 🔴 Bugs
    Explain bugs found.
    
    ## 🟠 Security Issues
    Explain security issues found.
    If none, say "None found."
    
    ## 🟡 Bad Practices
    Explain bad practices found.
    If none, say "None found."
    
    ## 🔵 Performance Problems
    Explain performance problems.
    If none, say "None found."
    
    ## 🟣 Edge Cases
    List important edge cases.
    
    ## 🟢 Improvements
    Give practical improvements.
    
    Rules:
    - Be concise.
    - Use bullet points.
    - Do not repeat the code unnecessarily.
    - Do not use JSON.
    - Do not add any sections other than the ones above.
    
    Code:
    {code}
    """
    
    response = call_ollama(prompt)
    

    return response