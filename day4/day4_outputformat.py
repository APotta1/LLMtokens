import ollama

data = "John Smith, age 34, software engineer, joined January 2023, salary $95000, department Engineering, manager Sarah Jones"

# NO FORMAT SPEC — model decides the format
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Extract the employee information from the text."},
        {"role": "user", "content": data}
    ],
    options={"temperature": 0}
)
print("=== No format specified ===")
print(response["message"]["content"])

print()

# WITH FORMAT SPEC — you control exactly what comes back
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": """Extract employee information from the text.

<output_format>
Return only a JSON object in exactly this structure, nothing else:
{
    "name": "",
    "age": 0,
    "role": "",
    "start_date": "",
    "salary": 0,
    "department": "",
    "manager": ""
}
</output_format>"""},
        {"role": "user", "content": data}
    ],
    options={"temperature": 0}
)
print("=== With format specified ===")
print(response["message"]["content"])