import ollama
import json
from datetime import datetime

# ── Tool implementations ──────────────────────────────────────────
# These are the actual functions that do the real work
# The model never runs these — your code does

def get_weather(city: str) -> dict:
    # In real life this would call a weather API
    # We're faking it so you can see the flow without an API key
    fake_weather = {
        "london":        {"temp": 12, "condition": "rainy"},
        "san francisco": {"temp": 18, "condition": "foggy"},
        "new york":      {"temp": 22, "condition": "sunny"},
        "tokyo":         {"temp": 28, "condition": "humid"},
    }
    data = fake_weather.get(city.lower(), {"temp": 20, "condition": "unknown"}) #lookup
    return {"city": city, "temp_celsius": data["temp"], "condition": data["condition"]} #output

def calculate(expression: str) -> dict:
    try:
        result = eval(expression)
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"error": str(e)}

def get_current_time() -> dict:
    now = datetime.now()
    return {"time": now.strftime("%H:%M"), "date": now.strftime("%Y-%m-%d")}

# ── Tool definitions ──────────────────────────────────────────────
# This is the menu you hand to the model
# Descriptions are prompt engineering — write them clearly

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city name"}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "The math expression to evaluate e.g. 2 + 2"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current time and date",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

# ── Tool dispatcher ───────────────────────────────────────────────
# Maps tool names to actual functions
# When the model requests a tool, this runs the right one

def run_tool(name: str, arguments: dict) -> str:
    if name == "get_weather":
        result = get_weather(**arguments)
    elif name == "calculate":
        result = calculate(**arguments)
    elif name == "get_current_time":
        result = get_current_time()
    else:
        result = {"error": f"Unknown tool: {name}"}
    return json.dumps(result)

# ── Main agent loop ───────────────────────────────────────────────

def chat(user_message: str):
    print(f"\nUser: {user_message}")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Only use tools when you need real-time data like current weather, live calculations, or the current time. For general knowledge questions you already know the answer to, respond directly without using any tools."},
        {"role": "user", "content": user_message}
    ]

    # First call — model decides if it needs a tool
    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=tools
    )

    message = response["message"]

    # If model wants a tool
    if message.get("tool_calls"):
        for tool_call in message["tool_calls"]:
            name = tool_call["function"]["name"]
            arguments = tool_call["function"]["arguments"]

            print(f"\n  → Model wants to call: {name}")
            print(f"  → With arguments: {arguments}")

            # Run the actual tool
            tool_result = run_tool(name, arguments)
            print(f"  → Tool returned: {tool_result}")

            # Add tool result to messages
            messages.append({"role": "tool", "content": tool_result})

        # Second call — model reads tool result and writes final response
        final_response = ollama.chat(
            model="llama3.2",
            messages=messages,
            tools=tools
        )
        print(f"\nAssistant: {final_response['message']['content']}")

    else:
        # Model didn't need a tool — just answered directly
        print(f"\nAssistant: {message['content']}")

# ── Test it ───────────────────────────────────────────────────────

chat("What is the weather like in London?")
chat("What is 1234 multiplied by 5678?")
chat("What time is it right now?")
chat("What is the capital of France?")  # no tool needed — model already knows this