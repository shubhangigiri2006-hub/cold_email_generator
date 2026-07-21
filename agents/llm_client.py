from groq import Groq #imports groq class from groq package
from config import GROQ_API_KEY, GROQ_MODEL #imports api key and model name from config file

_client = Groq(api_key=GROQ_API_KEY) #underscore client variable is an instance of the Groq class, initialized with the API key
#The underscore prefix is a convention to indicate that this variable is intended for internal use within the module and should not be accessed directly from outside.
#reduces unecessary setup time for each agent, since they all share the same client instance

def complete(system: str, user: str, max_tokens: int = 800, temperature: float = 0.7) -> str:
    """Single-turn completion helper shared by all agents."""
    response = _client.chat.completions.create(
        model=GROQ_MODEL,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return response.choices[0].message.content.strip()