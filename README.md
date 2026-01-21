AI Japanese Proficiency Assessment Assistant (N5–N3)
1. Problem Definition

Many Japanese learners are unsure about their current proficiency level (N5–N3) and often start learning materials that are either too easy or too difficult.

This project aims to build a simple AI assistant that estimates a learner’s Japanese proficiency level based on a short diagnostic test and provides learning recommendations.

2. Scope and Constraints

Target levels: JLPT N5, N4, N3

Test length: 15 multiple-choice questions

Skills evaluated:

Vocabulary

Grammar

Reading comprehension

Listening is excluded due to web limitations.

The system provides estimation, not official certification.

3. System Overview

User completes an online test.

Answers are scored by category.

An AI logic module evaluates the results using:

Rule-based evaluation

Similarity scoring

The assistant outputs:

Estimated JLPT level

Explanation of the result

Suggested next learning steps

4. AI Logic Design
4.1 Rule-based Evaluation

Each JLPT level has minimum score thresholds.

Example:

N5: Vocabulary ≥ 60%, Grammar ≥ 50%

N4: Vocabulary ≥ 70%, Grammar ≥ 60%

N3: Vocabulary ≥ 75%, Grammar ≥ 70%

Rules ensure the result is interpretable and explainable.

4.2 Similarity Scoring

Each JLPT level is represented as a skill profile vector.

Example:

User vector = [vocabulary, grammar, reading]
N4 profile  = [0.7, 0.6, 0.6]


Cosine similarity is used to determine which level best matches the user’s ability.

5. Result Interpretation

The final level is determined by combining:

Rule-based qualification

Highest similarity score

The assistant also explains why a certain level was chosen.

6. Limitations and Bias

Short tests may not fully reflect proficiency.

Guessing can affect results.

Learners strong in listening but weak in reading may be underestimated.

7. Future Improvements

Add listening section

Adaptive testing

Machine learning-based scoring

Personalized learning paths