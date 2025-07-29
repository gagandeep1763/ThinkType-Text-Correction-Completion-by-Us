from flask import Flask, request, jsonify
from flask_cors import CORS
from happytransformer import HappyTextToText, TTSettings

app = Flask(__name__)
CORS(app)

# Load the small T5 model
happy_tt = HappyTextToText("T5", "t5-small")
custom_args = TTSettings(num_beams=1, min_length=1, max_length=30)

@app.route("/")
def home():
    return "Grammar Correction & Text Completion API using T5-small"

@app.route("/correct", methods=["POST"])
def correct_text():
    data = request.get_json()
    input_text = data.get("text", "")
    result = happy_tt.generate_text("grammar: " + input_text, args=custom_args)
    return jsonify({"output": result.text})

@app.route("/complete", methods=["POST"])
def complete_text():
    data = request.get_json()
    input_text = data.get("text", "")
    result = happy_tt.generate_text("complete: " + input_text, args=custom_args)
    return jsonify({"output": result.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
