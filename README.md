# Resume Reviewer 📄

A Streamlit application that uses Claude AI to analyze resumes and provide actionable feedback. The app provides instant, AI-powered feedback on your resume to help improve its content and structure.

## Features

- 📤 Easy PDF upload interface
- 🤖 AI-powered resume analysis using Claude
- ⚡ Real-time feedback
- 🎯 Actionable improvement suggestions
- 📱 Clean, modern UI
- ☁️ Optional deployment to Modal Cloud

## Complete Guide: From Project Creation to Deployment

### 1. Project Setup

First, create a new project using `uv`:

```bash
# Create a new directory and initialize it
uv init resume-reviewer
cd resume-reviewer

# Initialize git repository
git init
```

### 2. Configure Dependencies

Create or update `pyproject.toml`:

```toml
[project]
name = "resume-reviewer"
version = "0.1.0"
description = "AI-powered resume reviewer using Claude"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "streamlit",
    "anthropic",
    "python-dotenv",
    "modal"
]
```

Install dependencies:
```bash
uv sync
```

### 3. Create GitHub Repository

Using GitHub CLI:
```bash
# Create a new repository
gh repo create resume-reviewer --public --description "AI-powered resume reviewer using Claude and Streamlit"

# Add files and make initial commit
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### 4. Create the Streamlit Application

Create `app.py`:
```python
import streamlit as st
import anthropic
import base64
import os

st.set_page_config(
    page_title="Resume Reviewer",
    page_icon="📄",
    layout="centered"
)

st.title("Resume Reviewer 📄")
st.write("Upload your resume and get instant feedback from AI!")

def analyze_resume(pdf_bytes):
    # Encode PDF
    pdf_data = base64.b64encode(pdf_bytes).decode("utf-8")
    
    # Initialize Claude client
    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"]
    )
    
    # Send to Claude
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data
                        }
                    },
                    {
                        "type": "text",
                        "text": "Analyze the resume and provide actionable feedback..."
                    }
                ]
            }
        ],
    )
    
    return message.content[0].text

# File uploader and UI logic...
```

### 5. Local Development

1. Create a `.env` file:
```bash
ANTHROPIC_API_KEY=your_api_key_here
```

2. Run locally:
```bash
uv run streamlit run app.py
```

### 6. Deploy to Modal (Optional)

1. Install Modal CLI and login:
```bash
pip install modal
modal token new
```

2. Create `serve_streamlit.py`:
```python
import shlex
import subprocess
from pathlib import Path
import modal

# Define the image with dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "streamlit~=1.35.0",
        "anthropic",
        "python-dotenv",
    )
    .copy_local_file("app.py", "/app/streamlit/app.py")
)

# Create the Modal app
app = modal.App(name="resume-reviewer")

@app.function(
    image=image,
    allow_concurrent_inputs=100,
    secrets=[modal.Secret.from_name("anthropic-secret")]
)
@modal.web_server(8000)
def run():
    target = shlex.quote("/app/streamlit/app.py")
    cmd = f"streamlit run {target} --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false"
    subprocess.Popen(cmd, shell=True)
```

3. Create Modal secret for Anthropic API key:
```bash
modal secret create anthropic-secret ANTHROPIC_API_KEY=<your-api-key>
```

4. Deploy to Modal:
```bash
modal deploy serve_streamlit.py
```

Your app will be available at `https://<your-username>--resume-reviewer-run.modal.run`

## Project Structure

```shell
resume-reviewer/
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── app.py                 # Main Streamlit application
├── serve_streamlit.py     # Modal deployment configuration
├── pyproject.toml         # Project dependencies and metadata
└── uv.lock               # Lock file for dependencies
```

## Development

To update dependencies:
```bash
uv sync
```

To upgrade specific packages:
```bash
uv lock --upgrade-package <package-name>
```

## Security Notes

- Never commit your `.env` file or expose your API keys
- Use Modal secrets for secure API key management in production
- The application processes resumes locally and only sends them to Claude for analysis
- No data is stored permanently

## License

[Your chosen license]
