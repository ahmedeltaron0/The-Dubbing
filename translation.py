import re
from deep_translator import GoogleTranslator
from transcription import transc

def word_tokenization(text):
    words = re.findall(r'\b\w+\b', text)
    return words

def translate(input_text):
    script_lang = "ar"
    max_chunk_length = 500
    words = word_tokenization(input_text)

    translated_chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) <= max_chunk_length:
            current_chunk += word + " "
        else:
            translated_chunk = GoogleTranslator(source='auto', target=script_lang).translate(current_chunk.strip())
            translated_chunks.append(translated_chunk)
            current_chunk = word + " "

    # Translate the last chunk
    if current_chunk:
        translated_chunk = GoogleTranslator(source='auto', target=script_lang).translate(current_chunk.strip())
        translated_chunks.append(translated_chunk)

    translated_text = " ".join(translated_chunks)

    # Save the transcription to a file
    output_file_path = "translation_output.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_text)

    return translated_text

if __name__ == "__main__":
    # Read the transcription from the saved file
    with open("transcription_output.txt", "r", encoding="utf-8") as input_file:
        transcription_result = input_file.read()

    translated_result = translate(transcription_result)
    print("Translated Result:", translated_result)
