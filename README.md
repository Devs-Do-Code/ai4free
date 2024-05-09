
<div align="center">
  <img src="https://img.shields.io/badge/Ai4Free-API-blue?style=for-the-badge&logo=huggingface" alt="HuggingChat API Badge">
  <h1>Free - Unofficial Reverse Engineered API 🚀</h1>
  <p>
    <a href="https://github.com/Devs-Do-Code/ai4free/stargazers">
      <img alt="GitHub stars" src="https://img.shields.io/github/stars/Devs-Do-Code/ai4free?style=social">
    </a>
    <a href="https://github.com/Devs-Do-Code/ai4free/network/members">
      <img alt="GitHub forks" src="https://img.shields.io/github/forks/Devs-Do-Code/ai4free?style=social">
    </a>
    <a href="https://github.com/Devs-Do-Code/ai4free/issues">
      <img alt="GitHub issues" src="https://img.shields.io/github/issues/Devs-Do-Code/ai4free?style=social">
    </a>
  </p>
</div>

<div align="center">
  <!-- Replace `#` with your actual links -->
  <a href="https://youtube.com/@devsdocode"><img alt="YouTube" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
  <a href="https://t.me/devsdocode"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
  <a href="https://www.instagram.com/sree.shades_/"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/developer-sreejan/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://buymeacoffee.com/devsdocode"><img alt="Buy Me A Coffee" src="https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black"></a>
</div>

# AI4Free: A Python Library for Free Access to All Available Large Language Models

AI4Free is a Python library that provides convenient access to a variety of large language models (LLMs) from different providers, all without requiring any API keys or fees. This allows developers and researchers to experiment with various LLMs and explore their capabilities without the barrier of cost.

## Crafted with ❤️ by Devs Do Code (Sree) and OEvortex

> **Disclaimer:** This project is not officially associated with Any Offical APIs. It is an independent reverse engineering effort to explore the All Available APIs.


## Features
- **Multiple LLM Providers:** AI4Free supports a diverse range of LLM providers including:
  - **Open-source LLMs:** KoboldAI, LEO (Brave AI)
  - **Free-tier access LLMs:** YouChat, OpenGPT, Yep
  - **Research/Demo access LLMs:** Phind, Blackbox
- **Conversation Management:** The library helps maintain conversation history with the LLMs, enabling more natural and context-aware interactions.
- **Prompt Optimization:** AI4Free includes built-in prompt optimization techniques to enhance the quality and relevance of generated responses.
- **Streaming Support:** Responses can be streamed in real-time, allowing for immediate feedback and dynamic interactions.
- **Asynchronous Capabilities:** Async versions of several providers are available for efficient handling of multiple requests and improved performance.

## Installation
```bash
pip install ai4free
```
**Use code with caution.**

## Usage
The basic usage pattern involves creating an instance of the desired LLM provider and then using the `chat()` method to interact with the model.

## Example Usage of Available Providers (Synchronous)

Here's how to use each of the available providers in AI4Free without asynchronous functions:

## LEO
```python
from ai4free import LEO

leo = LEO()

while True:
    prompt = input("You: ")
    response = leo.chat(prompt)
    print(f"LEO: {response}")
```


## KoboldAI
```python
from ai4free import KOBOLDAI

koboldai = KOBOLDAI()

while True:
    prompt = input("You: ")
    response = koboldai.chat(prompt)
    print(f"KoboldAI: {response}")
```


## Blackbox
```python
from ai4free import BLACKBOXAI

ai = BLACKBOXAI(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
    model=None # You can specify a model if needed
)

# Start an infinite loop for continuous interaction
while True:
    # Define a prompt to send to the AI
    prompt = input("Enter your prompt: ")
    
    # Check if the user wants to exit the loop
    if prompt.lower() == "exit":
        break
    
    # Use the 'chat' method to send the prompt and receive a response
    r = ai.chat(prompt)
    print(r)
```


## Phind
```python
from ai4free import PhindSearch

# Create an instance of the PHIND class
ph = PhindSearch()

# Define a prompt to send to the AI
prompt = "write a essay on phind"

response = ph.chat(prompt)
print(response)
```


## Yep
```python
from ai4free import YEPCHAT

# Instantiate the YEPCHAT class with default parameters
YEPCHAT = YEPCHAT()

# Define a prompt to send to the AI
prompt = "What is the capital of France?"

# Use the 'chat' method to get a response from the AI
r = YEPCHAT.chat(prompt)
print(r)
```


## YouChat
```python
from ai4free import YouChat

ai = YouChat(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

prompt = "what is meaning of life"

response = ai.ask(prompt)

# Extract and print the message from the response
message = ai.get_message(response)
print(message)
```

## Cohere
```python
from ai4free import Cohere

# Replace 'YOUR_API_KEY' with your Cohere API key
cohere = Cohere(api_key='YOUR_API_KEY')

while True:
    prompt = input("You: ")
    response = cohere.chat(prompt)
    print(f"Cohere: {response}")
```


## REKA
```python
from ai4free import REKA

# Replace 'YOUR_API_KEY' with your REKA API key
reka = REKA(api_key='YOUR_API_KEY')

while True:
    prompt = input("You: ")
    response = reka.chat(prompt)
    print(f"REKA: {response}")
```


## GROQ
```python
from ai4free import GROQ

# Replace 'YOUR_API_KEY' with your GROQ API key
groq = GROQ(api_key='YOUR_API_KEY')

while True:
    prompt = input("You: ")
    response = groq.chat(prompt)
    print(f"GROQ: {response}")
```

## Available Providers
- **Cohere:** Provides access to various text generation models including "command-r-plus" with capabilities like summarization, copywriting, and dialogue.
- **REKA:** Offers several LLM models like "reka-core", "reka-flash", and "reka-edge" for tasks such as question answering, text generation, and summarization.
- **GROQ:** Grants access to models like "mixtral-8x7b-32768" with capabilities for text generation, translation, and question answering.
- **LEO:** Provides access to "llama-2-13b-chat" with abilities for dialogue, text generation, and question answering.
- **KoboldAI:** Offers various open-source LLM models for text generation and creative writing.
- **OpenAI:** Enables interaction with OpenAI models like "gpt-3.5-turbo" for diverse tasks like text generation, translation, and code generation. Requires an API key.
- **OpenGPT:** Provides access to various LLM models for text generation and creative writing.
- **Blackbox:** Grants access to powerful LLMs for various tasks like text generation, translation, and question answering.
- **Phind:** Offers access to advanced LLMs with research and demo capabilities for tasks like text generation, code generation, and question answering.
- **Yep:** Provides access to models like "Mixtral-8x7B-Instruct-v0.1" with capabilities for text generation, translation, and question answering.
- **YouChat:** Offers free-tier access to a powerful LLM with abilities for dialogue, text generation, and question answering.

## Conclusion
AI4Free opens up exciting possibilities for exploring and utilizing the power of large language models without any cost. With its easy-to-use interface and support for diverse LLM providers, the library provides a valuable tool for developers, researchers, and anyone interested in exploring the cutting-edge of AI language technology.


<div align="center">
  <!-- Replace `#` with your actual links -->
  <a href="https://youtube.com/@devsdocode"><img alt="YouTube" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
  <a href="https://t.me/devsdocode"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
  <a href="https://www.instagram.com/sree.shades_/"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/developer-sreejan/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://buymeacoffee.com/devsdocode"><img alt="Buy Me A Coffee" src="https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black"></a>
</div>
