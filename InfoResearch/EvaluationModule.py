"""
@authors: CHASSANDE-YOU
"""

import time
import sys
import DictioManager
import VectorialModule
import BooleanModule
import PonderatorModule
import ProbabilistModule

def getTimeDictioDocID(file, common_words):
    # Dictio[docID, Dictio[word, occurence]]
    startTime = time.clock()
    DictioManager.CreateDictioFromFile(file, common_words)
    endTime = time.clock()
    print("Temps de calcul pour creation de Dictio[docID, Dictio[word, occurence]]: " + str(endTime - startTime))

    return (endTime - startTime)

def getTimeDictioWord(dictioDocID):
    # Dictio[word, Dictio[docID, occurence]]
    startTime = time.clock()
    DictioManager.CreateInverseDictio(dictioDocID)
    endTime = time.clock()
    print("Temps de calcul pour creation de Dictio[word, Dictio[docID, occurence]]: " + str(endTime - startTime))

    return (endTime - startTime)

def getTimePonderFreqNorm(dictioDocID, dictioWord):
    # Dictio[docID, Dictio[word, ponderationValueFreqNorm]]
    startTime = time.clock()
    PonderatorModule.UsePonderation(0, dictioDocID, dictioWord)
    endTime = time.clock()
    print("Temps de calcul pour creation de Dictio[docID, Dictio[word, ponderationValueFreqNorm]]: " + str(endTime - startTime))

    return (endTime - startTime)

def getTimePonderTFIDF(dictioDocID, dictioWord):
    # Dictio[docID, Dictio[word, ponderationValueTF-IDF]]
    startTime = time.clock()    
    PonderatorModule.UsePonderation(1, dictioDocID, dictioWord)
    endTime = time.clock()
    print("Temps de calcul pour creation de Dictio[docID, Dictio[word, ponderationValueTF-IDF]]: " + str(endTime - startTime))

    return (endTime - startTime)


def getTimeVectorialRequest(requestForVector, dictioWord, common_words):
    startTime = time.clock() 
    VectorialModule.VectorialRequest(requestForVector, dictioWord, common_words)
    endTime = time.clock()
    print("Temps de calcul pour reponse d'une requete vectorielle est: " + str(endTime - startTime))

    return (endTime - startTime)
 
def getTimeBooleanRequest(requestForBoolean, dictioWord, common_words):
    startTime = time.clock() 
    BooleanModule.BooleanRequest(requestForBoolean, dictioWord, common_words)
    endTime = time.clock()
    print("Temps de calcul pour reponse d'une requete booleenne est: " + str(endTime - startTime))

    return (endTime - startTime)     

def getTimeProbabilistRequest(requestForVector, dictioWord, dictioDocID, common_words):
    startTime = time.clock() 
    ProbabilistModule.ProbabilistRequest(requestForVector, dictioWord, dictioDocID, common_words)
    endTime = time.clock()
    print("Temps de calcul pour reponse d'une requete probabiliste est: " + str(endTime - startTime))

    return (endTime - startTime)  

def runEvaluation(common_words, dictioDocID, dictioWord, requestForVector, requestForBoolean):
    getTimeDictioWord(dictioDocID)
    getTimePonderFreqNorm(dictioDocID, dictioWord)
    getTimePonderTFIDF(dictioDocID, dictioWord)
    getTimeVectorialRequest(requestForVector, dictioWord, common_words)
    getTimeBooleanRequest(requestForBoolean, dictioWord, common_words)
    getTimeProbabilistRequest(requestForVector, dictioWord, dictioDocID, common_words)

def getDiskSize(dictioDocID, dictioWord, dictioPonderFreqNorm, dictioPonderTFIDF):
    print("La taille de Dictio[docID, Dictio[word, occurence]] est: " + str(sys.getsizeof(dictioDocID)) + " bytes.")
    print("La taille de Dictio[word, Dictio[docID, occurence]] est: " + str(sys.getsizeof(dictioWord)) + " bytes.")
    print("La taille de Dictio[docID, Dictio[word, ponderationValueFreqNorm]] est: " + str(sys.getsizeof(dictioPonderFreqNorm)) + " bytes.")
    print("La taille de Dictio[docID, Dictio[word, ponderationValueTF-IDF]]: est: " + str(sys.getsizeof(dictioPonderTFIDF)) + " bytes.")

def getPrecision(request, dictioWord, common_words):

    return 0

def getRecall():

    return 0

def getFMeasure(precision, recall):

    return 2 * (precision * recall) / (precision + recall)

def getEMeasure():

    return 0

def getRMeasure():

    return 0
