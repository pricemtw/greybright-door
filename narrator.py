import json
import os
import requests  # Built into Actions env

GROK_API_KEY = os.getenv("GROK_API_KEY")  # Set as repo secret
GROK_URL = "https://api.x.ai/v1/chat/completions"  # Grok-4 endpoint

def generate_response(world: dict, player_action: str) -> str:
    """Call Grok to narrate consistently from world state."""
    prompt = f"""
    You are the narrator for GREYBRIGHT DOOR, a persistent BBS-style RPG.
    World state: {json.dumps(world, indent=2)}
    Player action: "{player_action}"
    
    Rules:
    - Maintain 100% consistency: Names, descriptions, stats, gear NEVER change unless story-driven.
    - Keep responses immersive, 100-200 words, end with "What do you do?"
    - Update world only via JSON diffs in your response (e.g., if player kills NPC, mark dead).
    - BBS style: Dramatic, text-adventure feel.
    
    Respond ONLY with the narrative text. No JSON or extras.
    """
    
    headers = {"Authorization": f"Bearer {GROK_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "grok-4",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,
        "temperature": 0.7
    }
    
    response = requests.post(GROK_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"[Error: {response.status_code}] Default: The shadows deepen. What do you do?"
