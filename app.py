from flask import Flask, request, jsonify, render_template
from main import correct_text, complete_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocorrect', methods=['POST'])
def autocorrect():
    data = request.get_json()
    input_text = data.get('input', '')
    if not input_text:
        return jsonify({'output': 'No input provided'}), 400

    corrected = correct_text(input_text)
    return jsonify({'output': corrected})

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    input_text = data.get('input', '')
    if not input_text:
        return jsonify({'output': 'No input provided'}), 400

    completed = complete_text(input_text)
    return jsonify({'output': completed})

if __name__ == '__main__':
    app.run(debug=True)