import os 
from dotenv import load_dotenv
import openai

def gpt_definition(word, language):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [ 
            {"role": "system", "content": f"You are an {language} assistant"},
            {"role": "system", "content": "Please return the definition string"},
            {"role": "user", "content": word}
        ]
    )
    return response.choices[0]['message']['content']

def gpt_translate(word, language1, language2):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [ 
            {"role": "system", "content": f"You are a language translator from {language1} to {language2}"},
            {"role": "system", "content": "Please only return the translated word"},
            {"role": "user", "content": word}
        ]
    )
    return response.choices[0]['message']['content']

# only return correct phonetic when "word" in "language"
# need to translate the word before use 
def gpt_phonetic(word, language):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [ 
            {"role": "system", "content": f"You are a {language} phonetic pronunciation assitant"},
            {"role": "system", "content": "Please only return the phonetic pronunciation string"},
            {"role": "user", "content": word},
        ]
    )
    return response.choices[0]['message']['content']

def ask_gpt(message):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [ 
            {"role": "user", "content": input},
        ]
    )
    return response.choices[0]['message']['content']