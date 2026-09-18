# ChotuAI

A local AI developer assistant powered by Ollama.

## Features

- Generate Git commit messages
- Review complete files
- Review code snippets
- Choose any Ollama model installed locally

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running locally, with at least one model pulled
- Git (required since installation is via GitHub)

## Installation

pip install git+https://github.com/RiShI11-0902/Chotu-AI.git

## Setup

chotuai setup

## Usage

### 1. Configure ChotuAI

Before using the AI features, configure ChotuAI and select an Ollama model installed on your machine:

```bash
chotuai setup
```

ChotuAI will detect the Ollama models available on your machine and let you choose which model to use.

---

### 2. Generate a Git Commit Message

```bash
chotuai commit-message
```

Generates a concise commit message based on your **staged Git changes**.

Make sure you have staged your changes first:

```bash
git add .
```

Then run:

```bash
chotuai commit-message
```

Example:

```text
Suggested commit message:
feat: add user authentication
```

---

### 3. Review a File

```bash
chotuai review-file <filename>
```

Reviews the **entire contents of a file** and provides feedback about bugs, security issues, bad practices, performance problems, edge cases, and possible improvements.

Example:

```bash
chotuai review-file test.py
```

You can provide a relative or full file path:

```bash
chotuai review-file src/app.py
```

```bash
chotuai review-file "D:\projects\myapp\app.py"
```

The file must exist at the path you provide.

---

### 4. Review a Code Snippet

```bash
chotuai review-snippet
```

Use this when you want to review a **piece of code without creating or saving it as a file**.

After running the command, ChotuAI will ask you to paste your code:

```text
Paste your code below.
Type END or end on a new line when finished.
```

Paste your code, and when you are finished, type:

```text
END
```

Example:

```text
chotuai review-snippet

Paste your code below.
Type END on a new line when finished.

def add(a, b):
    return a + b

END
```

ChotuAI will then analyze the snippet and display the code review.

### Quick Reference

| Command                          | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| `chotuai setup`                  | Select an Ollama model for ChotuAI                |
| `chotuai commit-message`         | Generate a commit message from staged Git changes |
| `chotuai review-file <filename>` | Review an entire source code file                 |
| `chotuai review-snippet`         | Review a pasted code snippet                      |
