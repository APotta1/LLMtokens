import ollama
import time
import random

def call_with_retry(messages, max_retries=5, base_delay=1.0):
    """
    Call the API with exponential backoff and jitter.
    Retries automatically on failure.
    """
    for attempt in range(max_retries):
        try:
            response = ollama.chat(
                model="llama3.2",
                messages=messages
            )
            return response
        
        except Exception as e:
            # Check if we've used all retries
            if attempt == max_retries - 1:
                print(f"All {max_retries} attempts failed. Giving up.")
                raise
            
            # Exponential backoff — wait longer each retry
            delay = base_delay * (2 ** attempt)
            
            # Jitter — add randomness so retries don't all hit at once
            jitter = random.uniform(0, delay * 0.1)
            wait_time = delay + jitter
            
            print(f"Attempt {attempt + 1} failed: {e}")
            print(f"Waiting {wait_time:.2f} seconds before retry...")
            time.sleep(wait_time)

def simulate_rate_limit():
    """
    Simulate what happens when you send many requests quickly.
    In real life this would trigger a 429 from the API.
    """
    messages = [{"role": "user", "content": "Say hello in one word."}]
    
    print("=== Sending 5 rapid requests ===\n")
    
    for i in range(5):
        start = time.time()
        response = call_with_retry(messages)
        elapsed = time.time() - start
        print(f"Request {i+1}: {response['message']['content'].strip()} ({elapsed:.2f}s)")

def demonstrate_backoff():
    """
    Show the backoff timing clearly.
    """
    print("\n=== Backoff timing demonstration ===\n")
    
    base_delay = 1.0
    for attempt in range(5):
        delay = base_delay * (2 ** attempt)
        jitter = random.uniform(0, delay * 0.1)
        wait_time = delay + jitter
        print(f"Attempt {attempt + 1} failed → wait {wait_time:.2f} seconds")

simulate_rate_limit()
demonstrate_backoff()