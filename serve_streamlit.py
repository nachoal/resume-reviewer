import shlex
import subprocess
from pathlib import Path

import modal

# Define the image with all required dependencies
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