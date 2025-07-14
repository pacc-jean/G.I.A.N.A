from app.services.datasource import DATA

def generate_response(messages: list[dict], username: str = None) -> dict:
    """
    Generate a contextual reply and optionally trigger an action.
    Accepts full message history and optional username for personalization.
    """
    # ✅ 1. Use latest user message only
    last_user_msg = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "").strip()
    last_msg = last_user_msg.lower().lstrip(">")  # Normalize for command matching

    data = {}

    print("\n🔍 Message history received:")
    for m in messages:
        print(f"[{m['role']}] {m['content']}")
    print(f"\n Processing message: '{last_user_msg}' (normalized to '{last_msg}')")

    # 🎯 Handle core commands
    if last_msg == "clear":
        data["text"] = "Memory wiped. Nothing happened here. Absolutely nothing."
        data["action"] = "clear"

    elif last_msg == "exit":
        data["text"] = "Exiting chat. I’ll be here when you’re back."
        data["action"] = "exit"

    elif last_msg == "create":
        data["text"] = (
            "🚧 Project creation started.\n"
            "What's the name of your new project?"
        )
        data["action"] = "start_project"

    elif last_msg == "help":
        data["text"] = (
            "Here's what I can do:\n"
            "- `bio` → Show who Luca is + his skills\n"
            "- `list` or `projects` → List all Luca's projects\n"
            "- `select_{project_name}` → Show more about a specific project\n"
            "- `create` → Begin a new project creation sequence\n"
            "- `clear` → Clear the current conversation\n"
            "- `exit` → Close the chat session\n"
            "- `help` → You're literally reading it"
        )

    elif last_msg == "bio":
        data["text"] = f"{DATA['bio']}\n\n🛠 Skills:\n- " + "\n- ".join(DATA["skills"])

    elif last_msg in ["projects", "list", "list all projects"]:
        data["text"] = "Luca's Projects:\n\n" + "\n\n".join([
            f"🔹 {p['name']}:\n{p['description']}\n {p['link']}"
            for p in DATA["projects"]
        ])

    elif last_msg.startswith("select_"):
        project_key = last_msg.replace("select_", "").strip()
        project = next((p for p in DATA["projects"] if p["name"].lower() == project_key), None)
        if project:
            data["text"] = f"Selected Project: {project['name']}\n\n{project['description']}\n {project['link']}"
        else:
            data["text"] = f"Project '{project_key}' not found. Make sure the name matches exactly."

    elif any(word in last_msg for word in ["hello", "hi", "hey", "yo", "hiya"]):
        # ✅ 2. Use personalized greeting
        if username:
            data["text"] = (
                f"Hey {username.title()}! G.I.A.N.A here — fully loaded and operational\n"
                "Type `>help` to see what I can do, or just chat like a human."
            )
        else:
            data["text"] = (
                "Hey hey! G.I.A.N.A here — fully loaded and operational\n"
                "Type `>help` to see what I can do, or just chat like a human."
            )

    else:
        data["text"] = f"Hmm, I don’t know how to respond to that yet… try `>help` to see what I *can* do."

    return data
