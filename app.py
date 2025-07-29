from flask import Flask, render_template, request
from main import correct_text, complete_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""
    completed_text = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form["input_text"]
        if "correct" in request.form:
            corrected_text = correct_text(input_text)
        elif "complete" in request.form:
            completed_text = complete_text(input_text)

    return render_template(
        "index.html",
        input_text=input_text,
        corrected_text=corrected_text,
        completed_text=completed_text,
    )

if __name__ == "__main__":
    app.run(debug=True)
