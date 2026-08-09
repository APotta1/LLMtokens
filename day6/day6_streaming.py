import ollama
import time

prompt = "Explain how the internet works in simple terms"

#NON-Streaming waiting for everything
print("==Non-Streaming==")
start = time.time() #returns current time as a float

response = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "user", "content": prompt}],
    stream=False
)

end = time.time()
print(response["message"]["content"])
print(f"\nTime to first output: {end - start:.2f} seconds")
print(f"Total wait {end - start:.2f} seconds \n")

print("== Streaming == ")
start = time.time()
first_token_time = None

stream = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "user", "content": prompt}],
    stream = True
)

for chunk in stream:
    token = chunk["message"]["content"]
    if token and first_token_time is None:
        first_token_time = time.time()
        print(f"Time to first token {first_token_time - start:.2f} seconds \n")
    print(token, end = "", flush = True)

end = time.time()
print(f"\n\nTotal time: {end - start:.2f} seconds")