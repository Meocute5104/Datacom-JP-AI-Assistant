from collections import defaultdict
import math

# =========================
# JLPT Skill Profiles
# =========================
JLPT_PROFILES = {
    "N5": [0.6, 0.5, 0.4],
    "N4": [0.7, 0.6, 0.6],
    "N3": [0.8, 0.7, 0.7],
}

# =========================
# Rule-based thresholds
# =========================
RULES = {
    "N5": {"vocab": 0.5, "grammar": 0.4},
    "N4": {"vocab": 0.6, "grammar": 0.5},
    "N3": {"vocab": 0.7, "grammar": 0.6},
}

# =========================
# Similarity function
# =========================
def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0


# =========================
# Explanation generator
# =========================
def generate_explanation(level, confidence):
    if confidence >= 0.85:
        confidence_label = "High"
        message = (
            f"This result has high confidence. "
            f"Your performance closely matches the expected profile of JLPT {level}. "
            f"You are likely comfortable studying materials at this level."
        )

    elif confidence >= 0.70:
        confidence_label = "Medium"
        message = (
            f"This result has medium confidence. "
            f"Your skills partially match JLPT {level}, but there may be gaps between different areas. "
            f"Further practice can help confirm your level."
        )

    else:
        confidence_label = "Low"
        message = (
            f"This result has low confidence. "
            f"Your performance does not strongly match a single JLPT level profile. "
            f"This level should be considered an estimate."
        )

    return confidence_label, message


# =========================
# Main evaluation function
# =========================
def evaluate(results):
    scores = defaultdict(list)

    # Collect correct answers by skill type
    for r in results:
        scores[r["type"]].append(r["correct"])

    # Calculate final skill scores
    final_scores = {
        k: sum(v) / len(v) if v else 0
        for k, v in scores.items()
    }

    # User ability vector
    user_vector = [
        final_scores.get("vocab", 0),
        final_scores.get("grammar", 0),
        final_scores.get("reading", 0),
    ]

    # Rule-based qualification
    qualified_levels = []
    for level, rule in RULES.items():
        if final_scores.get("vocab", 0) >= rule["vocab"] and \
           final_scores.get("grammar", 0) >= rule["grammar"]:
            qualified_levels.append(level)

    # Similarity-based selection
    best_level = "N5"
    best_score = 0

    for level in qualified_levels:
        sim = cosine_similarity(user_vector, JLPT_PROFILES[level])
        if sim > best_score:
            best_score = sim
            best_level = level

    best_score = round(best_score, 2)

    # Generate explanation
    confidence_label, explanation = generate_explanation(best_level, best_score)

    return best_level, best_score, final_scores, confidence_label, explanation
