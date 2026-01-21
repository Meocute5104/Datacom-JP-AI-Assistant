from flask import Flask, render_template, request
from questions import questions
from logic import evaluate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        results = []

        for q in questions:
            user_answer = request.form.get(str(q["id"]))
            correct = 1 if user_answer == q["answer"] else 0
            results.append({
                "type": q["type"],
                "correct": correct
            })

        level, confidence, scores, confidence_label, explanation = evaluate(results)

        return render_template(
    "result.html",
    level=level,
    confidence=confidence,
    confidence_label=confidence_label,
    explanation=explanation,
    scores=scores
)

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
