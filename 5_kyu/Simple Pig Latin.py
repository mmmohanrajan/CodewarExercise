__author__ = "Mohan"

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !

"""

# my code
# def pig_it(text):
#     return " ".join([w[1:]+w[:1]+'ay' if w.isalnum() else w for w in text.split()])

import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)

print pig_it('Pig latin is ! cool')
