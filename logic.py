import math

JLPT_PROFILES = {
    "N5": [0.6, 0.5, 0.4],
    "N4": [0.7, 0.6, 0.6],
    "N3": [0.8, 0.7, 0.7],
}

RULES = {
    "N5": {"vocab": 0.6, "grammar": 0.5},
    "N4": {"vocab": 0.7, "grammar": 0.6},
    "N3": {"vocab": 0.75, "grammar": 0.7},
}


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)


def evaluate(scores):
    user_vector = [
        scores["vocab"],
        scores["grammar"],
        scores["reading"]
    ]

    qualified_levels = []

    for level, rule in RULES.items():
        if scores["vocab"] >= rule["vocab"] and scores["grammar"] >= rule["grammar"]:
            qualified_levels.append(level)

    best_level = "N5"
    best_score = 0

    for level in qualified_levels:
        sim = cosine_similarity(user_vector, JLPT_PROFILES[level])
        if sim > best_score:
            best_score = sim
            best_level = level

    return best_level, best_score
# from questions import get_correct_answer