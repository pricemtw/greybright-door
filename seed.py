import random
import json

def generate_world_seed(game_name: str, player_name: str) -> int:
    """Same inputs → same world forever."""
    base = hash((game_name, player_name, "GREYBRIGHT_v13"))
    random.seed(base)
    return abs(base) & 0xFFFFFFFFFFFFFFFF

def initialize_world(seed: int, player_name: str) -> dict:
    """Bootstrap the persistent world state."""
    random.seed(seed)
    world = {
        "seed": seed,
        "name": "Shadows of Ironspire",
        "player": {
            "name": player_name,
            "location": "Caer Dhu Battlements",
            "stats": {"hp": 100, "str": 10, "gold": 5},
            "inventory": ["rusted sword", "leather cloak"]
        },
        "locations": {
            "Caer Dhu Battlements": {
                "description": "Cold stone under a blood-red moon. Rain lashes the ruins. A torch flickers ahead.",
                "npcs": ["shadowy figure"],  # Will expand consistently
                "visited": True
            },
            "Town Square": {
                "description": "Cobblestones slick with mist. Garrick the Wanderer mutters about the old war—missing two fingers, as always.",
                "npcs": ["Garrick the Wanderer"],
                "visited": False
            }
        },
        "characters": {
            "Garrick the Wanderer": {
                "description": "Old man, ragged cloak, mutters about the war. Missing two fingers on left hand.",
                "stats": {"loyalty": 50, "secrets_known": 1},
                "gear": ["beggar's staff"]
            }
        },
        "turn_count": 0,
        "story_summary": "You awaken in the ruins of Caer Dhu, a fallen fortress on the edge of Ironspire. Whispers of ancient curses linger in the wind."
    }
    return world
