import os
import pandas as pd
from tqdm import tqdm
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

df = pd.read_csv("interns.csv")

with open("cold_email_prompt_v2.txt", "r") as f:
    base_prompt = f.read()

# Prepare new output columns
df["Subject"] = ""
df["Generated Email"] = ""

for i, row in tqdm(df.iterrows(), total=len(df)):
    person_prompt = f"""
Using the following cold email generation framework:

{base_prompt}

Generate an email to {row['FIRST NAME']} {row['LAST NAME']}, a {row['POSITION']} at {row['COMPANY']} based in {row['CITY']}, {row['STATE']}, {row['COUNTRY']}.
Industry: {row['INDUSTRY']}
Relevant Keywords: {row['KEYWORDS']}
LinkedIn: {row['HYPERLINK ROLE']}
Email: {row['EMAIL']}

The email should include a clear, professional subject line on the first line, then the body immediately after.
    """

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=person_prompt,
            temperature=0.7,
            max_output_tokens=800
        )

        text = response.output_text.strip()

        # Extract subject if formatted like "Subject: ..."
        if text.lower().startswith("subject:"):
            lines = text.split("\n", 1)
            subject = lines[0].replace("Subject:", "").strip()
            email_body = lines[1].strip() if len(lines) > 1 else ""
            df.at[i, "Subject"] = subject
            df.at[i, "Generated Email"] = email_body
        else:
            df.at[i, "Generated Email"] = text

    except Exception as e:
        print(f"Error on row {i}: {e}")
        df.at[i, "Generated Email"] = f"ERROR: {e}"

df.to_csv("generated_emails.csv", index=False)
print("✅ All emails generated and saved to generated_emails.csv")
