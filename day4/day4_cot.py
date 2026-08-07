# The purpose is to show you that how you ask affects how accurately the model answers.
#direc thought so no thought process
import ollama
problem = problem = "A store sells apples for $0.50 each and oranges for $0.75 each. Sarah buys 4 apples and 3 oranges. She pays with a $10 bill. How much change does she get?"

response = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "system", "content": "Answer the question. Return only the final answer"},
     {"role": "user", "content": problem}
     ],
    options = {"temperature": 0}
)
print("==Direct Answer==")
print(response["message"]["content"])
print()

#Chain of thought
response = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "system", "content": "Think through the problem step by step, then give the final answer at the end."},
    {"role": "user", "content": problem}
    ],
    options = {"temperature": 0}

)
print("==Chain of thought==")
print(response["message"]["content"])
#step by step process