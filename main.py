# main.py
import streamlit as st
import requests
import json

st.set_page_config(page_title="Job Offer Analyzer", layout="wide")
st.title("Job Offer Analyzer")

st.markdown("""
Upload your job offer or NDA document (PDF, DOCX) and see a summary of key details like salary, benefits, PTO, and NDA terms.
""")

# Upload file
uploaded_file = st.file_uploader("Upload your job offer", type=["pdf", "docx"])

if uploaded_file is not None:
    st.info("Processing document...")

    # Prepare the file for API call
    files = {"file": uploaded_file.getvalue()}

    # Replace this with your actual BDA project API endpoint
    BDA_API_ENDPOINT = "https://your-bda-project-endpoint.amazonaws.com/process"

    try:
        response = requests.post(BDA_API_ENDPOINT, files=files)
        response.raise_for_status()
        data = response.json()

        st.success("Document processed successfully!")

        # Display structured output
        st.subheader("Extracted Job Offer Information")
        st.write("**Base Salary:**", data.get("base_salary", "N/A"))
        st.write("**Signing Bonus:**", data.get("signing_bonus", "N/A"))
        st.write("**Equity / Stock Options:**", data.get("equity", "N/A"))
        st.write("**PTO:**", data.get("pto", "N/A"))
        st.write("**Healthcare Plan:**", data.get("healthcare_plan", "N/A"))
        st.write("**Start Date:**", data.get("start_date", "N/A"))
        st.write("**NDA / Legal Clauses:**", data.get("nda_terms", "N/A"))

    except requests.exceptions.RequestException as e:
        st.error(f"Error processing document: {e}")
