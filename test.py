import litellm
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()
litellm.suppress_debug_info = True

def generate_response(messages: List[Dict], model: str) -> str:
    response = litellm.completion(
        model=model,
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
    {"role": "user", "content": "Write a python function to swap the keys and values in a dictionary, minimal comments please."}
]

## Anthropic models, fast and capable
# response = generate_response(messages, "anthropic/claude-sonnet-4-20250514")

## Openrouter models, speed varies by model
#
# response = generate_response(messages, "openrouter/google/gemini-2.5-flash-lite") 
# response = generate_response(messages, "openrouter/xiaomi/mimo-v2-flash:free")
response = generate_response(messages, "openrouter/deepseek/deepseek-v3.2")
print(response)

## Huggingface models, works but much slower than openrouter
#
# response = generate_response(messages, "huggingface/together/deepseek-ai/DeepSeek-R1")
response = generate_response(messages, "huggingface/zai-org/GLM-4.7-Flash")
print(response)
