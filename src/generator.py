import pandas as pd
from typing import List, Dict
import os

def generate_excel(data: List[Dict], output_path: str = "output/final_output.xlsx"):
    """
    Converts parsed JSON data (list of dicts) into an Excel file.
    Columns: Key, Value, Comments
    """

    df = pd.DataFrame(data)

    # Ensure correct column order
    expected_cols = ["key", "value", "comments"]
    df = df.reindex(columns=expected_cols)

    # Create output folder if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_excel(output_path, index=False)

    print(f"Excel generated at: {output_path}")


if __name__ == "__main__":
    # For testing only
    sample = [
        {"key": "Name", "value": "Usha", "comments": "Example"},
        {"key": "Role", "value": "AI Intern", "comments": "Example"},
    ]

    generate_excel(sample)
