"""
@authors: CHASSANDE-YOU
"""

import re
import math
from operator import itemgetter


""" Return a list of docID containing the words in the request (request pattern: (A B C)), given a DictioWord """
def VectorialRequest(request, dictioWord, common_words):
    listDoc = list()
    dictioSimil = dict()
    dictioRequest = dict()
    requeteLength = 0
    dictioLength = dict()
    
    # Filtering words from request
    words = re.findall(r"[\w']+", request)
    filtered_words = list([i.lower() for i in words if i.lower() not in common_words])
    
    for word in filtered_words:
        if(word in dictioRequest):
            actualsize = dictioRequest[word]
            dictioRequest[word] = actualsize + 1
        else:
            dictioRequest[word] = 1
    #print(dictioRequest)
    for word in dictioRequest:
        if word in dictioWord:
            for docID in dictioWord[word]:
                if docID in dictioSimil:
                    actualsize = dictioSimil[docID]
                    dictioSimil[docID] = actualsize + dictioWord[word][docID] * dictioRequest[word]
                    actualsize = dictioLength[docID]
                    dictioLength[docID] = actualsize + dictioWord[word][docID] * dictioWord[word][docID]
                else:
                    dictioSimil[docID] = dictioWord[word][docID] * dictioRequest[word]
                    dictioLength[docID] = dictioWord[word][docID] * dictioWord[word][docID]
        requeteLength += dictioRequest[word]*dictioRequest[word]
    for docID in dictioSimil:
        actualsize = dictioSimil[docID]
        dictioSimil[docID] = round(actualsize / (math.sqrt(requeteLength) * math.sqrt(dictioLength[docID])), 12)
    #remplir une liste des documents tries par similarite
    listDoc = sorted(dictioSimil.items(), key=itemgetter(1), reverse = True)
    #print(listDoc[0:100])
    return listDoc
