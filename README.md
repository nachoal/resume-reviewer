# Resume Reviewer 📄

A Streamlit application that uses Claude AI to analyze resumes and provide actionable feedback. The app provides instant, AI-powered feedback on your resume to help improve its content and structure.

## Features

- 📤 Easy PDF upload interface
- 🤖 AI-powered resume analysis using Claude
- ⚡ Real-time feedback
- 🎯 Actionable improvement suggestions
- 📱 Clean, modern UI

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral/uv) package manager
- An Anthropic API key

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd resume-reviewer
```

2. Initialize the project with uv:
```bash
uv init --app
```

3. Create or update pyproject.toml with dependencies:
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
    "python-dotenv"
]
```

4. Sync the dependencies:
```bash
uv sync
```

5. Create a `.env` file in the project root and add your Anthropic API key:
```bash
ANTHROPIC_API_KEY=your_api_key_here
```

## Running the Application

Start the Streamlit server:
```bash
uv run streamlit run hello.py
```

The application will be available at `http://localhost:8501`

## Usage

1. Open the application in your web browser
2. Upload your resume in PDF format
3. Click "Analyze Resume"
4. Wait for the AI to analyze your resume
5. Review the feedback and suggestions

## Project Structure

```shell
resume-reviewer/
├── .env                # Environment variables (API keys)
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
├── hello.py           # Main Streamlit application
├── pyproject.toml     # Project dependencies and metadata
└── uv.lock            # Lock file for dependencies
```

## Development

To update dependencies in pyproject.toml:

1. Edit the dependencies list in pyproject.toml
2. Run sync to update the environment:
```bash
uv sync
```

To upgrade specific packages:
```bash
uv lock --upgrade-package <package-name>
```

## Security Notes

- Never commit your `.env` file or expose your API keys
- The application processes resumes locally and only sends them to Claude for analysis
- No data is stored permanently

## License

[Your chosen license]
