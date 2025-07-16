import streamlit as st
from summarizer import generate_summary

st.set_page_config(page_title="Text Summarizer", layout="centered")
st.title("📝 Generative Text Summarizer")
st.markdown("Paste any long-form content below and click **Summarize** to generate a concise version.")

# Text input
input_text = st.text_area("Enter your text here:", height=300)

# Summarize button
if st.button("Summarize") and input_text.strip():
    with st.spinner("Generating summary..."):
        try:
            summary = generate_summary(input_text)
            st.subheader("🧠 Summary")
            st.success(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
