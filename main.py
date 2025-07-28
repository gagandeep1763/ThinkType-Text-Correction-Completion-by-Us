from happytransformer import HappyTextToText, TTSettings

# Load the T5 model for grammar correction and text completion
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

# Create custom generation settings
custom_args = TTSettings(num_beams=1, min_length=1, max_length=30)

def correct_text(text):
    result = happy_tt.generate_text("grammar: " + text, args=custom_args)
    return result.text

def complete_text(text):
    result = happy_tt.generate_text("complete: " + text, args=custom_args)
    return result.text