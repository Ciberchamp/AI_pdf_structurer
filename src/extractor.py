import pdfplumber
import os

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extracts ALL text from a PDF while preserving original line breaks.
    """
    full_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)

    return "\n".join(full_text)


if __name__ == "__main__":
    # For testing
    sample_path = "samples/Data_Input.pdf"
    if os.path.exists(sample_path):
        txt = extract_pdf_text(sample_path)
        print(txt[:1000])  # print first 1000 chars
    else:
        print("PDF not found. Place Data_Input.pdf inside samples/")
