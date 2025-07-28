from flask import Flask, request, jsonify, render_template
from main import correct_text, complete_text

app = Flask(__name__)

# Home route to render frontend
@app.route('/')
def index():
    return render_template('index.html')  # Make sure 'index.html' exists inside the 'templates' folder

# Route for grammar correction
@app.route('/autocorrect', methods=['POST'])
def autocorrect():
    data = request.get_json()
    input_text = data.get('input', '').strip()

    if not input_text:
        return jsonify({'output': 'No input provided'}), 400

    try:
        corrected = correct_text(input_text)
        return jsonify({'output': corrected})
    except Exception as e:
        return jsonify({'output': f'Error: {str(e)}'}), 500

# Route for text completion
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    input_text = data.get('input', '').strip()

    if not input_text:
        return jsonify({'output': 'No input provided'}), 400

    try:
        completed = complete_text(input_text)
        return jsonify({'output': completed})
    except Exception as e:
        return jsonify({'output': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)