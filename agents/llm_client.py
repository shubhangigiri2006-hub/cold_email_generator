from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

_client = Groq(api_key=GROQ_API_KEY)


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