import re
import inflect
from googletrans import Translator

def convert_text_to_arabic(text):
    def replace_with_arabic(match):
        numerical_value = int(match.group())
        p = inflect.engine()
        arabic_form = p.number_to_words(numerical_value, andword=", و")
        return arabic_form

    def replace_word_with_arabic(match):
        numeric_word = match.group()
        translator = Translator()
        arabic_translation = translator.translate(numeric_word, src='en', dest='ar').text
        return arabic_translation

    # Regular expression to find numerical values and numeric words in the text
    numerical_pattern = re.compile(r'\b\d+\b')
    numeric_word_pattern = re.compile(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b', re.IGNORECASE)

    # Replace numerical values with Arabic written forms
    arabic_text = numerical_pattern.sub(replace_with_arabic, text)

    # Replace numeric words with their Arabic translations
    arabic_text = numeric_word_pattern.sub(replace_word_with_arabic, arabic_text)

    return arabic_text

def main():
    try:
        input_text = input("Enter a text: ")

        # Convert numerical values and numeric words in the text to Arabic
        converted_text = convert_text_to_arabic(input_text)

        print(f"The original text: {input_text}")
        print(f"The modified text with Arabic numbers: {converted_text}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
