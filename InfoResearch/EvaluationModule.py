"""
@authors: CHASSANDE-YOU
"""

import time
import sys
import re
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


# Use moduleInt == 0 to do a vectorial request and 1 to do a boolean request. The dictioRequest can be either dictioPonderFreqNormWord or dictioPonderTFIDFWord 
def getPrecision(listRequest, moduleInt, dictioListDocID_TP, dictioRequest, common_words):
    listPrecision = []
    result = 0
    
    for request in listRequest:
        index = listRequest.index(request)
        if(index in dictioListDocID_TP.keys()):
            if moduleInt == 0:
                # Vectorial Request     
                listVectorialDocID = VectorialModule.VectorialRequest(request, dictioRequest, common_words)
                pertinent = 0
                for i in listVectorialDocID:
                    if i[0] in dictioListDocID_TP[index]:
                        if i[1] > 0:
                            pertinent += 1
                if(len(listVectorialDocID) != 0):
                    result = pertinent / len(listVectorialDocID)
                else :
                    result = 0

            elif moduleInt == 1:
                # Boolean Request
                listBooleanDocID = BooleanModule.BooleanRequest(request, dictioRequest, common_words)
                pertinent = 0
                for i in listBooleanDocID:
                    if i[0] in dictioListDocID_TP[index]:
                        if i[1] > 0:
                            pertinent += 1
                if(len(listBooleanDocID) != 0):
                    result = pertinent / len(listBooleanDocID)
                else:
                    result = 0
        
            else: 
                result = 0
            # At position i, precision for request i + 1    
            listPrecision.append(result)
    return listPrecision

# Use moduleInt == 0 to do a vectorial request and 1 to do a boolean request. The dictioRequest can be either dictioPonderFreqNormWord or dictioPonderTFIDFWord 
def getRecall(listRequest, moduleInt, dictioListDocID_TP, dictioRequest, common_words):
    listPrecision = []
    result = 0
    
    for request in listRequest:
        index = listRequest.index(request)
        if(index in dictioListDocID_TP.keys()):
            if moduleInt == 0:
                # Vectorial Request     
                listVectorialDocID = VectorialModule.VectorialRequest(request, dictioRequest, common_words)
                pertinent = 0
                for i in listVectorialDocID:
                    if i[0] in dictioListDocID_TP[index]:
                        if i[1] > 0:
                            pertinent += 1

                result = pertinent / len(dictioListDocID_TP[index])

            elif moduleInt == 1:
                # Boolean Request
                listBooleanDocID = BooleanModule.BooleanRequest(request, dictioRequest, common_words)
                pertinent = 0
                for i in listBooleanDocID:
                    if i[0] in dictioListDocID_TP[index]:
                        if i[1] > 0:
                            pertinent += 1

                result = pertinent / len(dictioListDocID_TP[index])

            else: 
                result = 0
            # At position i, precision for request i + 1    
            listPrecision.append(result)
    return listPrecision

# Use beta == 1 for equal ponderation on precision and recall
def getE_Measure(beta, precision, recall):
    x = beta * beta
    return (1 - ((x + 1) * precision * recall) / (x * precision + recall ))

def getF_Measure(beta, precision, recall):
    return (1 - getE_Measure(beta, precision, recall))


def getR_Measure():
    #TODO
    return 0
