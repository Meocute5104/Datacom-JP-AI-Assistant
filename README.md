# AI Japanese Proficiency Assessment Assistant (N5–N3)

## Overview
This project implements the core logic of a simple AI assistant that estimates a learner’s Japanese language proficiency level (JLPT N5–N3) based on a short diagnostic test.

The assistant analyzes the test results and provides:
- An estimated JLPT level
- An explanation of how the result was determined
- A confidence score based on similarity matching

The goal of this project is not to build a full-scale product, but to demonstrate problem definition, reasoning, and explainable AI logic.

---

## Problem Definition
Many Japanese learners are unsure about their current proficiency level and often choose learning materials that are either too easy or too difficult.

This project addresses that problem by helping learners **estimate their current JLPT level** using a short test and a transparent evaluation process.

---

## Scope and Constraints
- Target levels: **JLPT N5, N4, N3**
- Test length: short diagnostic test (conceptual: 10–15 questions)
- Skills evaluated:
  - Vocabulary
  - Grammar
  - Reading comprehension
- Listening is excluded due to web and time constraints.
- The system provides **estimation**, not official certification.

---

## System Overview
The system operates in the following steps:

1. The user completes a diagnostic test.
2. Answers are scored by skill category.
3. The AI assistant evaluates the results using:
   - Rule-based evaluation
   - Similarity scoring
4. The system outputs:
   - Estimated JLPT level
   - Confidence score
   - Explanation of the decision

---

## AI Logic Design

### Rule-based Evaluation
Each JLPT level has minimum score thresholds for vocabulary and grammar.

Example:
- N5: Vocabulary ≥ 60%, Grammar ≥ 50%
- N4: Vocabulary ≥ 70%, Grammar ≥ 60%
- N3: Vocabulary ≥ 75%, Grammar ≥ 70%

These rules ensure that higher levels are only considered when basic requirements are met.

---

### Similarity Scoring
Each JLPT level is represented as a predefined skill profile vector:
N5 = [0.6, 0.5, 0.4]
N4 = [0.7, 0.6, 0.6]
N3 = [0.8, 0.7, 0.7]

The user’s performance is converted into a vector:

Cosine similarity is used to measure how closely the user’s performance matches each JLPT profile.  
The level with the highest similarity score (among rule-qualified levels) is selected.

---

## Decision Strategy
The final decision combines:
- **Rule-based filtering** (to ensure minimum competence)
- **Similarity-based ranking** (to select the best-matching level)

This hybrid approach balances interpretability and flexibility.

---

## Limitations and Bias
- Short tests may not fully represent actual proficiency.
- Guessing may inflate scores.
- Learners strong in listening but weak in reading may be underestimated.
- Skill profiles are manually designed and may introduce bias.

These limitations are acknowledged as part of the system design.

---

## Technology Stack
- Language: **Python**
- Framework: **Flask**
- Frontend: Simple HTML templates
- Deployment: Local environment only

---

## How to Run Locally

```bash
pip install flask
python app.py

Then open:

http://127.0.0.1:5000
