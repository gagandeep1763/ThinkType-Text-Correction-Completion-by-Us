from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline
from happytransformer import HappyTextToText, TTSettings

app = Flask(__name__)
CORS(app)

# Load autocomplete model (GPT-2)
autocomplete_pipe = pipeline('text-generation', model='gpt2')

# Load autocorrect model (T5 fine-tuned for grammar correction)
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
tt_settings = TTSettings(num_beams=5, min_length=1)

# Serve HTML using Flask's template system
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocorrect', methods=['POST'])
def autocorrect():
    input_text = request.json['input']
    # Use T5 grammar correction
    result = happy_tt.generate_text("grammar: " + input_text, args=tt_settings)
    corrected_text = result.text
    return jsonify({'output': corrected_text})

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    input_text = request.json['input']
    input_word_count = len(input_text.split())
    # Set max_length to input length + 10, but at least 20 for short inputs
    max_length = max(input_word_count + 10, 20)
    result = autocomplete_pipe(
        input_text,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=autocomplete_pipe.model.config.eos_token_id,
        do_sample=True,
        top_p=0.95,
        top_k=50
    )
    generated = result[0]['generated_text']
    # Only return the part after the input, limited to 10 words
    completion = generated[len(input_text):].strip()
    completion_words = completion.split()
    limited_completion = ' '.join(completion_words[:10])
    return jsonify({'output': limited_completion})

if __name__ == '__main__':
    app.run(debug=True)
