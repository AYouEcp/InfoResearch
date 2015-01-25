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


# Use moduleInt == 0 to do a vectorial request and 1 to do a boolean request. The dictioRequest can be either dictioPonderFreqNormWord or dictioPonderTFIDFWord 
def getPrecision(request, moduleInt, dictioWord, dictioRequest, common_words):
    result = 0
    
    if moduleInt == 0:
        # Filtering words from request
        words = re.findall(r"[\w']+", request)
        filtered_words = list([i.lower() for i in words if i.lower() not in common_words])   
        
        for word in filtered_words:
            listDocID_TP = []
            for i in dictioWord[wordClean]:
                listDocID_TP.append(i)
        
        listVectorialDocID = VectorialModule.VectorialRequest(request, dictioRequest, common_words)
        pertinent = 0
        for i in listVectorialDocID:
            if i in listDocID:
                pertinent += 1

        result = pertinent / len(listVectorialDocID)

    elif moduleInt == 1:
        # Parsage string with AND (each substring has a (A OR B OR NOT C) pattern)
        substrings = request.split(" AND ")
        # Parsage substrings with OR (each word has a "(A" or "B" or "NOT C" or "D)" pattern)
        for substring in substrings:                
            # Array Partiel for OR
            arrayPartiel = [0 for i in range(dictioLength)] 
            words = substring.split(" OR ")
            for word in words:
                # Remove "(", ")" (each word has a "A" or "NOT B" pattern)
                wordClean = word.replace("(", "").replace(")", "").replace("NOT", "").replace(" ","").lower()
                
                listDocID_TP = []
                for i in dictioWord[wordClean]:
                    listDocID_TP.append(i)
    
        listBooleanDocID = BooleanModule.BooleanRequest(request, dictioRequest, common_words)
        pertinent = 0
        for i in listBooleanDocID:
            if i in listDocID:
                pertinent += 1

        result = pertinent / len(listBooleanDocID)

    else: 
        result = 0
    
    return result

# Use moduleInt == 0 to do a vectorial request and 1 to do a boolean request. The dictioRequest can be either dictioPonderFreqNormWord or dictioPonderTFIDFWord 
def getRecall(request, moduleInt, dictioWord, dictioRequest, common_words):
    result = 0
    
    if moduleInt == 0:
        # Filtering words from request
        words = re.findall(r"[\w']+", request)
        filtered_words = list([i.lower() for i in words if i.lower() not in common_words])   
        
        for word in filtered_words:
            listDocID_TP = []
            for i in dictioWord[wordClean]:
                listDocID_TP.append(i)
        
        listVectorialDocID = VectorialModule.VectorialRequest(request, dictioRequest, common_words)
        pertinent = 0
        for i in listVectorialDocID:
            if i in listDocID:
                pertinent += 1

        result = pertinent / len(listDocID_TP)

    elif moduleInt == 1:
        # Parsage string with AND (each substring has a (A OR B OR NOT C) pattern)
        substrings = request.split(" AND ")
        # Parsage substrings with OR (each word has a "(A" or "B" or "NOT C" or "D)" pattern)
        for substring in substrings:                
            # Array Partiel for OR
            arrayPartiel = [0 for i in range(dictioLength)] 
            words = substring.split(" OR ")
            for word in words:
                # Remove "(", ")" (each word has a "A" or "NOT B" pattern)
                wordClean = word.replace("(", "").replace(")", "").replace("NOT", "").replace(" ","").lower()
                
                listDocID_TP = []
                for i in dictioWord[wordClean]:
                    listDocID_TP.append(i)
    
        listBooleanDocID = BooleanModule.BooleanRequest(request, dictioRequest, common_words)
        pertinent = 0
        for i in listBooleanDocID:
            if i in listDocID:
                pertinent += 1

        result = pertinent / len(listDocID_TP)

    else: 
        result = 0
    
    return result

# Use beta == 1 for equal ponderation on precision and recall
def getE_Measure(beta, precision, recall):
    x = beta * beta
    return (1 - ((x + 1) * precision * recall) / (x * precision + recall ))

def getF_Measure(beta, precision, recall):
    return (1 - getE_Measure(beta, precision, recall))


def getR_Measure():
    #TODO
    return 0
