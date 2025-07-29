from happytransformer import HappyTextToText

# Load the grammar correction model
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

def correct_text(text):
    result = happy_tt.generate_text("grammar: " + text, args={"max_length": 50})
    return result.text

def complete_text(text):
    result = happy_tt.generate_text("complete: " + text, args={"max_length": 50})
    return result.text