import anthropic
import time

# pip install anthropic first
client = anthropic.Anthropic()

# A long system prompt — in real life this might be
# detailed instructions, examples, or a large document
SYSTEM_PROMPT = """You are an expert software engineer with deep knowledge of 
Python, system design, and AI engineering. You give precise, accurate answers.

Here are some examples of how you respond:

Q: What is a context manager in Python?
A: A context manager is an object that defines __enter__ and __exit__ methods,
used with the 'with' statement to manage resources like files or database 
connections. It guarantees cleanup even if an error occurs.

Q: What is the difference between a list and a tuple?
A: Lists are mutable sequences using square brackets. Tuples are immutable 
sequences using parentheses. Use tuples for fixed data, lists for data that 
changes. Tuples are slightly faster and can be used as dictionary keys.

Q: What is a decorator in Python?
A: A decorator is a function that takes another function as input and returns
a modified version of it. Used with @syntax to add behaviour like logging,
timing, or authentication without modifying the original function directly.
""" * 10  # repeat to make it long enough to cache (min ~1024 tokens)

questions = [
    "What is a generator in Python?",
    "What is the GIL?",
    "What is a closure?",
]

for i, question in enumerate(questions):
    start = time.time()
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"}  # ← this marks it for caching
            }
        ],
        messages=[
            {"role": "user", "content": question}
        ]
    )
    
    elapsed = time.time() - start
    usage = response.usage
    
    print(f"\nQuestion {i+1}: {question}")
    print(f"Answer: {response.content[0].text[:100]}...")
    print(f"Time: {elapsed:.2f}s")
    print(f"Input tokens:        {usage.input_tokens}")
    print(f"Cache write tokens:  {getattr(usage, 'cache_creation_input_tokens', 0)}")
    print(f"Cache read tokens:   {getattr(usage, 'cache_read_input_tokens', 0)}")