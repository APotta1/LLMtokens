import ollama

response = ollama.chat(
    model = "llama3.2",
    messages = [
        {"role": "system", "content": "Classify the sentiment of the text as POSITIVE, NEGATIVE, or NEUTRAL. Return only the label, nothing else."},
        {"role": "user", "content": "The battery life on this laptop is disappointing."}
    ]
)
print("=== Zero-shot (no examples) ===")
print(response["message"]["content"])

print()


#purpose of zero-shot examples you are expecting the model with no examples
#You are trusting it to give the format

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Classify the sentiment of the text as POSITIVE, NEGATIVE, or NEUTRAL. Return only the label, nothing else."},
        {"role": "user", "content": "This phone has an amazing camera."},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "The package arrived on time."},
        {"role": "assistant", "content": "NEUTRAL"},
        {"role": "user", "content": "I waited 45 minutes and the food was cold."},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "The battery life on this laptop is disappointing."}
    ]
)
print("=== Few-shot (3 examples) ===")
print(response["message"]["content"])



# What text goes in — the messages array you build
# How the model behaves — system prompt, temperature, few-shot examples
# What text comes out — the response you print


# When you give it few-shot examples you're not teaching it anything new. You're saying "match this specific pattern for this conversation."

# See the format → copy the format
# See the style → copy the style
# See the classification logic → copy the logic