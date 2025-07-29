# ThinkType
ThinkType – Text Correction & Completion by Us
A simple web-based application that performs grammar correction and text completion using a pre-trained transformer model (T5).

![ThinkType Screenshot](https://github.com/gagandeep1763/ThinkType-Text-Correction-Completion-by-Us/blob/main/image.png?raw=true)

ThinkType is a lightweight and effective tool for improving user-typed text.  
It offers two key features:

- **Autocorrect:** Automatically corrects grammar and spelling errors in the input.
- **Autocomplete:** Suggests possible text completions for partially typed sentences.

This project is fully built from scratch using Python (Flask) and the [Happy Transformer](https://github.com/EricFillion/happy-transformer) library.

---

## Features

- Built using Flask for backend
- Uses Happy Transformer with T5 model for NLP tasks
- Minimal and clean UI with gradients
- Responsive layout
- Easy to extend or deploy

---

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/gagandeep1763/ThinkType-Text-Correction-Completion-by-Us
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python app.py
    ```

4. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

---

## Project Structure

```
├── app.py
├── main.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## Model Used

- [`vennify/t5-base-grammar-correction`](https://huggingface.co/vennify/t5-base-grammar-correction)

---

## Credits

Developed entirely by us for learning and implementation purposes.  
No third-party UI templates used.

**Developed By:**  
Gagandeep D  
Google Certified UI/UX Designer  & 
Aspiring Data Analyst
