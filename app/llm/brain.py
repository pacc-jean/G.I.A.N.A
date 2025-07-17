import requests

def generate_response(messages: list[dict], username: str = None) -> dict:
    """
    Send message history to Ollama (Mistral) and return the model's response.
    """

    prompt = [
        {"role": m["role"], "content": m["content"]}
        for m in messages
    ]

    if username:
        system_prompt = {
            "role": "system",
            "content": (
                f"You are G.I.A.N.A, a clever and witty AI assistant created by Luca. "
                f"You're helpful, poetic, and talk like Gen Z but still give serious answers. "
                f"The user you're helping is named {username.title()}."
            )
        }
        prompt.insert(0, system_prompt)

    try:
        res = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",
                "messages": prompt,
                "stream": False
            },
            timeout=120
        )

        res.raise_for_status()
        data = res.json()

        return {"text": data.get("message", {}).get("content", ""), "action": None}

    except Exception as e:
        print("❌ Error generating response:", e)
        return {"text": "Hmm… something went wrong with my brain (LLM connection failed).", "action": None}

