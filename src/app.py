import streamlit as st
import os
import pandas as pd
from extractor import extract_pdf_text
from parser import parse_with_ai
from generator import generate_excel

st.set_page_config(page_title="AI PDF → Excel Converter", layout="wide")

st.title("📄 → 📊 AI-Powered PDF to Excel Structurer")
st.write("Upload any unstructured PDF and convert it into a clean, structured Excel file.")

# Upload widget
uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_pdf:

    # Save temporarily
    save_path = "temp_input.pdf"
    with open(save_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    st.success("PDF uploaded successfully!")

    # Extract text
    with st.spinner("Extracting text from PDF..."):
        raw_text = extract_pdf_text(save_path)

    st.text_area("Extracted Text (Preview)", raw_text, height=300)

    # Parse
    with st.spinner("Structuring data using AI..."):
        structured_data = parse_with_ai(raw_text)

    st.success("AI structuring completed!")

    # Convert to DataFrame for display
    df = pd.DataFrame(structured_data)
    st.dataframe(df, use_container_width=True)

    # Generate Excel file
    output_path = "output/final_output.xlsx"
    generate_excel(structured_data, output_path)

    # Download button
    with open(output_path, "rb") as f:
        st.download_button(
            label="📥 Download Excel Output",
            data=f,
            file_name="Output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    st.success("Excel ready for download!")

st.write("---")
st.write("Built with ❤️ using Streamlit + Groq + Python")
