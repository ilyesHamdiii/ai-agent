# Cipher

Cipher is a command-line coding assistant powered by Google Gemini, designed to help you interact with and manage Python projects.

---

## Why Cipher?

Cipher was created to simplify working with Python projects from the command line. It helps automate repetitive tasks, provides quick access to project information, and assists with code management, all without leaving your terminal.

---

## Motivation

Managing and navigating codebases can be time-consuming, especially when switching between tools. Cipher aims to keep everything in one place, making it easier to focus on development and problem-solving.

---

## 🚀 Fast Start Guide

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/ai-agent.git
cd ai-agent
```

### 2. Set Up Python

Make sure you have **Python 3.13+** installed.

Check your version:

```sh
python3 --version
```

### 3. Create a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

Or, if using `pyproject.toml`:

```sh
pip install .
```

### 5. Configure Your API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the Assistant

```sh
python main.py "your prompt here" [--verbose]
```

**Example:**

```sh
python main.py "List all files in the calculator directory"
```

---

## 📁 Project Structure

- `main.py` - Entry point for the assistant
- `call_function.py` - Handles function calls from the assistant
- `functions/` - File and execution operations
- `calculator/` - Example Python project
- `tests.py` - Utility tests

---

## 🛠 Requirements

- Python 3.13+
- See `pyproject.toml` for dependencies

---
