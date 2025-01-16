import anthropic
import base64
import os

# Load and encode the local PDF
pdf_path = "./pdfs/resume.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF file not found at {pdf_path}")

# Read and encode the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_data = base64.b64encode(pdf_file.read()).decode("utf-8")

# Send to Claude
client = anthropic.Anthropic()
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
                    "text": "Analyze the resume and provide actionable feedback in case of any issues. If the resume is good, just say 'The resume is good.'."
                }
            ]
        }
    ],
)

print(message.content)
