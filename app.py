from flask import Flask, render_template, request
from logic import evaluate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        scores = {
            "vocab": float(request.form["vocab"]),
            "grammar": float(request.form["grammar"]),
            "reading": float(request.form["reading"]),
        }

        level, confidence = evaluate(scores)
        return render_template(
            "result.html",
            level=level,
            confidence=round(confidence, 2)
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
