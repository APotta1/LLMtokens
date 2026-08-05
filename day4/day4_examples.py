import ollama

# JUST POSITIVE — only showing what you want
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": """You are a customer support agent for a software company.
        
<instructions>
Respond to customer complaints professionally and helpfully.
</instructions>

<example>
Customer: Your app keeps crashing and I lost all my work.
Response: I'm really sorry to hear that. Let me help you recover your work and fix the crashing issue right away.
</example>"""},
        {"role": "user", "content": "Your software is terrible, I've been waiting 3 days for a fix!"}
    ],
    options={"temperature": 0}
)
print("=== Positive example only ===")
print(response["message"]["content"])

print()

# POSITIVE AND NEGATIVE — showing what you want and don't want
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": """You are a customer support agent for a software company.

<instructions>
Respond to customer complaints professionally and helpfully.
Keep responses under 2 sentences.
</instructions>

<good_example>
Customer: Your app keeps crashing and I lost all my work.
Response: I'm really sorry to hear that. Let me help you recover your work and fix the crashing issue right away.
</good_example>

<bad_example>
Customer: Your app keeps crashing and I lost all my work.
Response: Have you tried turning it off and on again? Also make sure your internet is working.
</bad_example>"""},
        {"role": "user", "content": "Your software is terrible, I've been waiting 3 days for a fix!"}
    ],
    options={"temperature": 0}
)
print("=== Positive and negative examples ===")
print(response["message"]["content"])