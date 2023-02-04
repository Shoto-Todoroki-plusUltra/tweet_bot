import tracery
from tracery.modifiers import base_english
import json

def get_text():
    rules = json.loads(open("tracery_json.json").read())

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    text = grammar.flatten("#origin#")
    
    return str(text)