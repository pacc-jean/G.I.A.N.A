import requests
from app.core.config import Config

def generate_response(messages: list[dict], username: str = None) -> dict:
    """
    Send message history to Ollama and return the model's response.
    Uses env/config for model + host + timeout.
    """

    # Build chat-style history
    prompt = [{"role": m["role"], "content": m["content"]} for m in messages]

    if username:
        prompt.insert(0, {
            "role": "system",
            "content": (
                f"You are G.I.A.N.A, a clever, witty AI assistant created by Luca. "
                f"Speak with a poetic Gen Z vibe but deliver clear, correct help. "
                f"The user is {username.title()}."
            )
        })

    try:
        res = requests.post(
            f"{Config.OLLAMA_HOST}/api/chat",
            json={
                "model": Config.OLLAMA_MODEL,
                "messages": prompt,
                "stream": False,
                "options": {
                    "num_predict": 80,
                    "temperature": 0.7,
                }
            },
            timeout=Config.OLLAMA_TIMEOUT,
        )
        res.raise_for_status()
        data = res.json()
        text = data.get("message", {}).get("content", "").strip()
        if not text:
            text = "[No response 🤔]"
        return {"text": text, "action": None}

    except requests.exceptions.Timeout:
        print("🕒 Ollama timeout.")
    except requests.exceptions.ConnectionError:
        print("🔌 Cannot reach Ollama at", Config.OLLAMA_HOST)
    except requests.exceptions.HTTPError as err:
        print(f"📡 Ollama HTTP {err.response.status_code}: {err.response.text}")
    except Exception as e:
        print("❌ Unexpected Ollama error:", e)

    return {
        "text": "My brain’s offline (LLM connection failure). Try again in a sec.",
        "action": None,
    }
