import ollama

document = """
The quarterly earnings report shows revenue of $2.3M, up 12% from last quarter.
Customer acquisition cost dropped from $45 to $38. Churn rate increased slightly
from 2.1% to 2.4%. The new product launch in September contributed $340K in revenue.
Net profit margin sits at 18%, down from 21% due to increased hiring costs.
"""

# BAD — no structure, instructions and content blurred together
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Summarize the document and extract the key metrics as bullet points"},
        {"role": "user", "content": document}
    ],
    options={"temperature": 0}
)
print("=== No structure ===")
print(response["message"]["content"])

print()

# GOOD — XML tags clearly separate instructions from content
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": """You are a financial analyst.

<instructions>
Summarize the document inside <document> tags.
Extract all numeric metrics as bullet points.
Return only the summary and bullet points, nothing else.
</instructions>"""},
        {"role": "user", "content": f"""<document>
{document}
</document>"""}
    ],
    options={"temperature": 0}
)
print("=== With XML structure ===")
print(response["message"]["content"])