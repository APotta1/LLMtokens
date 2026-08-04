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

#0 -> always picks the top choice -> repeatable
#higher -> samples randomly, weighted by confidence -> varied and more varied the higher you go
# temperature 1 _> confidence loosely, 0 wins every single time which repeats itself