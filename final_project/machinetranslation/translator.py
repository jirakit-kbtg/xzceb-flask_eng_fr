"""
This module translate English string to French string and vice versa
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text:str)->str:
    """Translate from english to french"""
    mts = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = mts.translate(english_text)
    return french_text

def french_to_english(french_text:str)->str:
    """Translate from french to english"""
    mts = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = mts.translate(french_text)
    return english_text
