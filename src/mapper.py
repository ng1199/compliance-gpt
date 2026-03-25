from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def map_controls(controls1, controls2):
    mappings = []

    for c1 in controls1:
        best_match = None
        best_score = 0

        for c2 in controls2:
            score = similarity(c1["description"], c2["description"])
            if score > best_score:
                best_score = score
                best_match = c2

        mappings.append({
            "control_1": c1["description"],
            "control_2": best_match["description"] if best_match else "",
            "similarity_score": round(best_score, 2)
        })

    return mappings