import ollama

prompt = "Give me one creative name for a coffee shop. Just the name, nothing else."

print("=== temperature 0 (should be identical) ===")
for i in range(5):
    response = ollama.chat(
        model = "llama3.2",
        messages =[{"role": "user", "content": prompt}],
        options = {"temperature": 0 }
    )

    print(f"Run {i+1}: {response['message']['content'].strip()}")

print()
print("=== temperature 1 (should vary) ===")
for i in range(5):
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 1}
    )
    print(f"Run {i+1}: {response['message']['content'].strip()}")
