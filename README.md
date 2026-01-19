# LLM Lab

LiteLLM SDK gives you a unified interface to access multiple LLMs (100+ LLMs). Litellm allows us to connect directly to foundational models such as Antropics' Claude or OpenAI's GPT-3.5. It also allows us to connect to hundreds of them through Hugging Face (model hosting) or OpenRouter (model routing) services.

try out all llm models and providers and middlewares such as openrouter, litellm, etc...

## Setup
In .env, set the following environment variables:
``` 
HF_TOKEN=your_huggingface_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
OPENROUTER_API_BASE=https://openrouter.ai/api/v1 # optional

## References

### OpenRouter
OR allows us to connect to any LLMs without having to rewrite your code. See [LiteLLM and OpenRouter](https://docs.litellm.ai/docs/providers/openrouter) and [OpenRouter Models](https://openrouter.ai/models)

### Hugging Face
HF allows us to host and runus your own trained model. See [LiteLLM and Hugging Face](https://docs.litellm.ai/docs/providers/huggingface) and [Hugging Face Models](https://huggingface.co/docs/hub/models)

### Ollama
Ollama allows  to run a locally hosted LLM.
[LiteLLM and Ollama](https://docs.litellm.ai/docs/providers/ollama) and [Ollama Doc](https://docs.ollama.com/)

### Other Individual Providers

- [LiteLLM and Anthropic](https://docs.litellm.ai/docs/providers/anthropic)
- [LiteLLM and OpenAI](https://docs.litellm.ai/docs/providers/openai)
