# ThinkType
ThinkType – Text Correction & Completion by Us
A simple web-based application that performs grammar correction and text completion using a pre-trained transformer model (T5).

Overview
ThinkType is a lightweight and effective tool for improving user-typed text. It offers two key features:

Autocorrect: Automatically corrects grammar and spelling errors in the input.

Autocomplete: Suggests possible text completions for partially typed sentences.

This project is fully built from scratch using Python (Flask) and the happytransformer library.

Features: 
Built using Flask for backend

Uses Happy Transformer with T5 model for NLP tasks

Minimal and clean UI with gradients

Responsive layout

Easy to extend or deploy

How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/thinktype.git
cd thinktype
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000/

Project Structure
cpp
Copy
Edit
├── app.py
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── (optional: css or js files if added)
├── requirements.txt
└── README.md
Model Used
vennify/t5-base-grammar-correction

Powered by the HappyTextToText interface of HappyTransformer

Credits
Developed entirely by us for learning and implementation purposes.
No third-party UI templates used.

