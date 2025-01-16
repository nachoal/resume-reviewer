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
    
    # Initialize Claude client with API key from environment
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
                        "text": "Analyze the resume and provide actionable feedback in case of any issues. If the resume is good, just say 'The resume is good.'."
                    }
                ]
            }
        ],
    )
    
    return message.content[0].text

# File uploader
uploaded_file = st.file_uploader("Choose your resume PDF", type="pdf")

if uploaded_file is not None:
    # Show the PDF preview
    st.write("Preview of uploaded PDF:")
    st.write(f"Filename: {uploaded_file.name}")
    
    # Create a button to trigger analysis
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing your resume... This may take a few moments."):
            try:
                # Get the PDF bytes
                pdf_bytes = uploaded_file.getvalue()
                
                # Get analysis
                analysis = analyze_resume(pdf_bytes)
                
                # Display results in a nice format
                st.success("Analysis Complete! 🎉")
                st.markdown("### Feedback:")
                st.markdown(analysis)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")
                st.write("Please try again or contact support if the issue persists.") 