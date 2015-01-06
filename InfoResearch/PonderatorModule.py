"""
@authors: CHASSANDE-YOU
"""

import math

""" Ponderation Frequence Normalisee, return Dictio[word, ponderationValueFreqNorm] for a docID dictionary"""
def PonderateFreqNorm(dictio):
    dictioReturned = dict()
    maxFreq = 0

    # Get max frequency
    for word in dictio:
        if(dictio[word] > maxFreq):
            maxFreq = dictio[word]
    # Add word to dictioReturn with Ponderate Frequency
    for word in dictio:
        dictioReturned[word] = dictio[word] / maxFreq

    return dictioReturned

""" Ponderation TF-IDF, return Dictio[word, ponderationValueTF-IDF] for a docID dictionary"""
def PonderateTFIDF(dictio, dictioDocID, dictioWord):
    dictioReturned = dict()
    maxFreq = 0

    # Calculate TF-IDF for a word and get max TF-IDF
    for word in dictio:
        dictioReturned[word] = math.log(dictio[word] + 1) * math.log(len(dictioDocID) / len(dictioWord[word]))
        if(dictioReturned[word] > maxFreq):
            maxFreq = dictioReturned[word]
    # Add word to dictioReturn with TF-IDF Frequency
    for word in dictioReturned:
        actualValue = dictioReturned[word]
        dictioReturned[word] = actualValue / maxFreq 

    return dictioReturned

""" Return Dictio[docID, Dictio[word, ponderationValue]]. Use ponderationType == 0 for a Frequency Normalization Ponderation, and anything else for a TF-IDF Ponderation"""
def UsePonderation(ponderationType, dictioDocID, dictioWord):
    dictioReturned = dict()
    
    for docID in dictioDocID:
        if(ponderationType == 0):
            dictioReturned[docID] = PonderateFreqNorm(dictioDocID[docID])
        else:
            dictioReturned[docID] = PonderateTFIDF(dictioDocID[docID], dictioDocID, dictioWord)

    return dictioReturned