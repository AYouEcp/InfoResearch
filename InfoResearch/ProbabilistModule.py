"""
@authors: CHASSANDE-YOU
"""

import re
import math
from operator import itemgetter


""" Return a list of docID containing the words in the request (request pattern: (A B C)) """
def ProbabilistRequest(request, dictioWord, dictioDocID, common_words):
    listDoc = list()
    dictioRequest = dict()
    dictioSimil = dict()
    dictioQi = dict()

    # Filtering words from request
    words = re.findall(r"[\w']+", request)
    filtered_words = list([i.lower() for i in words if i.lower() not in common_words])
    
    for word in filtered_words:
        if(word in dictioWord):
            dictioRequest[word] = 1

    # size of dictioDocID = number of documents
    nbOfDoc = len(dictioDocID)

    # We choose a fixed value for pi
    p = 0.7

    # Create the dict containing qi values (proportion of documents containing the word ti)
    for word in dictioWord:
        dictioQi[word] = len(word) / len(dictioDocID)

    # Calculate RSV
    for doc in dictioDocID:
        RSV = 0
        for word in dictioDocID[doc]:
            if (word in dictioRequest):
                RSV += math.log10(p*(1-dictioQi[word])/(dictioQi[word]*(1-p)))
        dictioSimil[doc] = RSV

    listDoc = sorted(dictioSimil.items(), key=itemgetter(1), reverse = True)
    #print(listDoc[0:100])

    return listDoc