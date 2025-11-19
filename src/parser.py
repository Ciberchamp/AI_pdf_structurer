import os
import json
from groq import Groq
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def clean_llm_output(content: str) -> str:
    """
    Cleans LLM output by removing markdown and extracting pure JSON.
    """
    content = content.strip()

    # Remove ```json ... ``` blocks
    if "```" in content:
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    # Try to extract JSON part if model wraps it
    first_bracket = content.find("[")
    last_bracket = content.rfind("]")

    if first_bracket != -1 and last_bracket != -1:
        content = content[first_bracket:last_bracket + 1].strip()

    return content


def parse_with_ai(raw_text: str) -> List[Dict]:
    """
    Sends raw text to Groq LLM and gets clean structured JSON output.
    """

    prompt = f"""
You are an AI system that extracts structured information from a document.

### RULES (VERY IMPORTANT)
- Output MUST be ONLY valid JSON.
- NO markdown.
- NO backticks.
- NO code blocks.
- NO headings.
- NO extra words AT ALL.
- STRICTLY return ONLY a JSON ARRAY of objects.
- Keys must be CLEAN and GENERIC. Do NOT include the person's name in the key.
- DO NOT generate keys like "Vijay Kumar’s birthplace" or "Vijay Kumar’s age".
### JSON STRUCTURE (STRICT)
[
  {{
    "key": "original key text",
    "value": "exact extracted value (preserve wording)",
    "comments": "context pulled from PDF"
  }}
]

### TASK
From the text below, extract:
- Every possible key:value relationship
- Preserve exact wording from the PDF
- Do NOT summarize
- Do NOT paraphrase
- Include all contextual details in `comments`
- Ensure 100% coverage of the document

### TEXT:
{raw_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    cleaned = clean_llm_output(content)

    try:
        data = json.loads(cleaned)
        return data

    except Exception as e:
        # return raw for debugging
        return [{
            "key": "PARSING_ERROR",
            "value": cleaned,
            "comments": str(e)
        }]


if __name__ == "__main__":
    print("parser.py loaded successfully")
