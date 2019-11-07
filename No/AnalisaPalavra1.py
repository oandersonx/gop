from spellchecker import SpellChecker
def analisaPalavra(msg):
    
    
    spell = SpellChecker()
    
    
    erradas = spell.unknown(msg)
    l = []
    
    for i in erradas:
        l.append(spell.correction(i))
       
        
   
    return list(erradas)