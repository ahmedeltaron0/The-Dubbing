import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def generate_openai_response(question, temperature=0.7):
    messages = [{"role": "user", "content": f"You asked: {question}"}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"].strip()

def read_translation_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        translated_text = file.read()
    return translated_text

if __name__ == "__main__":
    # Specify the path to the translation file in the root folder
    translation_file_path = r"E:\Lip Sync\translation_output.txt"
    # Read the translated text from the file
    translated_text = read_translation_from_file(translation_file_path)

    # Create a simpler question without explicitly stating not to change any word
    user_question = "Proofread the following article :"
    
    # Combine the question and the translated text
    full_text = f"{user_question}\n{translated_text}"

    # Get the proofread response using GPT-3.5-turbo
    openai_response = generate_openai_response(full_text)

    print("GPT-3.5-turbo Response:", openai_response)
