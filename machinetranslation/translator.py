"""
Module translates from english to french and vs via IBM language_translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey="_gW7_yKKuIUY7BjNqAUJONMib9sqw5VaS6tb8ZeXi_a2"
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a96b3dcd-8b2d-42d4-bb9c-fb5104947161" 

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text: str):
    """Function takes the string in englsh and return translated string in french"""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        #Getting the pure translation string
        french_text = translation['translations'][0]['translation']
        return french_text
    except Exception as error:
        print(error)
        return None


def french_to_english(french_text: str):
    """Function takes the string in french and return translated string in english"""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        #Getting the pure translation string
        english_text = translation['translations'][0]['translation']
        return english_text
    except Exception as error:
        print(error)
        return None
