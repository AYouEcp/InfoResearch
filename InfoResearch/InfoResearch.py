"""
@authors: CHASSANDE-YOU
"""

import DictioManager
import VectorialModule
import BooleanModule
import PonderatorModule
import ProbabilistModule
import EvaluationModule
import time

file = open('cacm.all','r')
common_words = open('common_words', 'r').read()

requestForVector = "system computer tables"
requestForBoolean = "(system OR NOT computer) AND tables"      

# Dictio[docID, Dictio[word, occurence]]
""" WARNING: When getTimeDictioDocID runs, the other tests failed """
#EvaluationModule.getTimeDictioDocID(file, common_words)
dictioDocID = DictioManager.CreateDictioFromFile(file, common_words)

# Dictio[word, Dictio[docID, occurence]]
#EvaluationModule.getTimeDictioWord(dictioDocID)
dictioWord = DictioManager.CreateInverseDictio(dictioDocID)

# Dictio[docID, Dictio[word, ponderationValueFreqNorm]]
#EvaluationModule.getTimePonderFreqNorm(dictioDocID, dictioWord)
dictioPonderFreqNorm = PonderatorModule.UsePonderation(0, dictioDocID, dictioWord)

# Dictio[docID, Dictio[word, ponderationValueTF-IDF]]
#EvaluationModule.getTimePonderTFIDF(dictioDocID, dictioWord)
dictioPonderTFIDF = PonderatorModule.UsePonderation(1, dictioDocID, dictioWord)

# Dictio[word, Dictio[docID, ponderationValueFreqNorm]]
dictioPonderFreqNormWord = DictioManager.CreateInverseDictio(dictioPonderFreqNorm)

# Dictio[word, Dictio[docID, ponderationValueTF-IDF]]
dictioPonderTFIDFWord = DictioManager.CreateInverseDictio(dictioPonderTFIDF)
 

# Get the result of a vectorial request
#EvaluationModule.getTimeVectorialRequest(requestForVector, dictioWord, common_words)
VectorialModule.VectorialRequest(requestForVector, dictioWord, common_words)

# Get the result of a boolean request   
#EvaluationModule.getTimeBooleanRequest(requestForBoolean, dictioWord, common_words)
BooleanModule.BooleanRequest(requestForBoolean, dictioWord, common_words)

# Get the result of a probabilistic request   
#EvaluationModule.getTimeProbabilistRequest(requestForBoolean, dictioWord, common_words)
ProbabilistModule.ProbabilistRequest(requestForVector, dictioWord, dictioDocID, common_words)

# Performances evaluation
EvaluationModule.runEvaluation(common_words, dictioDocID, dictioWord, requestForVector, requestForBoolean)
EvaluationModule.getDiskSize(dictioDocID, dictioWord, dictioPonderFreqNorm, dictioPonderTFIDF)
