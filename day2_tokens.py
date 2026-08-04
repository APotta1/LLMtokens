import genericpath  # a real 200-line file from Python's own standard library

import tiktoken

enc = tiktoken.get_encoding("cl100k_base")  # OpenAI GPT-4 / 3.5-turbo; a rough proxy for other models

# __file__ is the path to a module's source, so this works on any machine
with open(genericpath.__file__, encoding="utf-8") as f:
    real_file = f.read()

texts = {
    "single word": "hello",
    "long word": "uncharacteristically",
    "prose": "Machine learning models learn by adjusting internal parameters.",
    "python code": "def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a+b\n    return a",
    "json": '{"model": "gpt-4", "messages": [{"role": "user", "content": "hello"}]}',
    "200-line file": real_file,
}

for label, text in texts.items():
    tokens = enc.encode(text)
    print(f"{label:20s} → {len(tokens):3d} tokens  ({len(text)/len(tokens):.1f} chars/tok)")
assert enc.decode(enc.encode(real_file)) == real_file
print("round-trip OK")

#tokenizers
# A launguage model is a big pile of math. Math operates on numbers not letters.
# so before any text reachs th emodel something has to convert hello into numbers
# That converter is the tokenizer

#tiktoken is a small open-source python library from open AI that does encode/decode on machine
#cl100k_base is the tokenizer for specific vocabulary
#cl - the family name, 100k - 100,000 tokens, base - base version

#generic path a 200-line file from Pythons own standard library