# 🔍 AI-Powered PDF → Excel Structurer

A fully automated **AI-backed document parsing system** that converts an unstructured PDF into a clean, structured Excel sheet.  
Built using **Python**, **Groq LLM**, and **Streamlit**, this project demonstrates intelligent data extraction, key–value detection, contextual understanding, and dynamic structuring.

## 🚀 Live Demo

Try the live hosted app here:  
👉 **https://aipdfstructurer-kbnrstgdarcrbrqkpy7bot.streamlit.app/**

## 🎥 Demo

🔗 **[Demo Video]**  
*https://drive.google.com/file/d/1amOXH10k_w--gcttBno7G4weiqvndR5n/view?usp=sharing*

---

## 📌 Project Overview

This project takes an **unstructured narrative-style PDF** and transforms it into a **professional, structured Excel output** following the exact requirements of the assignment:

- Extract **100% of the content**
- Identify key:value relationships
- Preserve **original wording**
- Add **meaningful contextual comments**
- Output a clean, tabular Excel file

## 🧱 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Groq Llama 3 (via Groq API) |
| PDF Parsing | pdfplumber, PyMuPDF |
| Excel Generation | Pandas, OpenPyXL |
| Deployment | Streamlit Cloud |

---
## steps to run the project

1. Clone the repo
- git clone https://github.com/Ciberchamp/AI_pdf_structurer.git
- cd AI_pdf_structurer

2. Create .env
- GROQ_API_KEY=your_api_key_here

3. Install dependencies
- pip install -r requirements.txt

4. Run the Streamlit app
- streamlit run src/app.py



