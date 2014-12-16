"""
@authors: CHASSANDE-YOU
"""

import DictioManager
import VectorialModule
import BooleanModule
import PonderatorModule

file = open('cacm.all','r')
common_words = open('common_words', 'r').read()

# Dictio[docID, Dictio[word, occurence]]
dictioDocID = DictioManager.CreateDictioFromFile(file, common_words)

# Dictio[word, Dictio[docID, occurence]]
dictioWord = DictioManager.CreateInverseDictio(dictioDocID)

# Dictio[word, Dictio[docID, ponderationValueFreqNorm]]
dictioPonderFreqNorm = PonderatorModule.UsePonderation(0, dictioDocID, dictioWord)

# Dictio[word, Dictio[docID, ponderationValueTF-IDF]]
dictioPonderTFIDF = PonderatorModule.UsePonderation(1, dictioDocID, dictioWord)

requestForVector = "system computer tables"
VectorialModule.VectorialRequest(requestForVector, dictioWord, common_words)

requestForBoolean = "(system OR NOT computer) AND tables"          
BooleanModule.BooleanRequest(requestForBoolean, dictioWord, common_words)

