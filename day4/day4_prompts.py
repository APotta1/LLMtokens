import ollama

response = ollama.chat(
    model = "llama3.2",
    messages= [
        {"role": "user", "content": "You are a professional editor. Fix the grammar in this sentence: i went to store and buyed milk"}
    ]
)
print("==Mixed User Role===")
print(response["message"]["content"])
print()

response = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "system", "content": "You are a professional editor. Fix grammar errors in whatever text the user sends. Return only the corrected sentence, nothing else."},
        {"role": "user", "content": "i went to store and buyed milk"}
    ]
)
print("=== System for instructions, user for input ===")
print(response["message"]["content"])

#reuse the real reason
#instructions stick better
#safety - the one that matters later
#multi-turn conversations need it