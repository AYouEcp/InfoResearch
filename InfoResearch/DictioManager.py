"""
@authors: CHASSANDE-YOU
"""

import re

""" Return a DictioDocID : Dictio[docID, Dictio[word, occurence]] where word is in file and not in common_words """
def CreateDictioFromFile(file, common_words):
    dictioGlobal = dict()
    dictioLocal = dict()
    docID = -1
    insert = False

    for line in file.readlines():

        if(line.startswith('.I')):            
            # If not first doc, insert dictioLocal
            if(docID != -1):
                dictioGlobal[docID] = dictioLocal
            
            # Get docID and reset dictioLocal when we open a new doc
            dictioLocal = dict()
            docID = int(line.split(' ')[1].replace("\n",""))
            insert = False

        elif(line.startswith('.T') | line.startswith('.W') | line.startswith('.K')):
            insert = True

        elif(line.startswith('.A') | line.startswith('.B') | line.startswith('.N') | line.startswith('.X')):
             insert = False

        elif(insert):
            words = re.findall(r"[\w']+", line)
            filtered_words = list([i.lower() for i in words if i.lower() not in common_words])

            for word in filtered_words:
                if(word in dictioLocal):
                    actualOccurence = dictioLocal[word]
                    dictioLocal[word] = actualOccurence + 1
                else :
                    dictioLocal[word] = 1

    return dictioGlobal

""" Return a DictioWord : Dictio[word, Dictio[docID, occurence]] from a given DictioDocID dictionary"""
def CreateInverseDictio(dictioDocID):
    dictioInverse = dict()

    for docID in dictioDocID:
        for word in dictioDocID[docID]:

            if word in dictioInverse:
                # Not sure if this condition can happend..., just the else is necessary
                if docID in dictioInverse[word]:
                    actualsize = dictioInverse[word][docID]
                    dictioInverse[word][docID] = actualsize + dictioDocID[docID][word]
                else:
                    dictioInverse[word][docID] = dictioDocID[docID][word]
            else:
                dictioLocal = dict()
                dictioLocal[docID] = dictioDocID[docID][word]
                dictioInverse[word] = dictioLocal
    
    return dictioInverse 

""" Return Dictio[word, occurence] for a given docID """
def WordsFromDocID(docID):
    return dictGlobal[docID]

""" Return Dictio[docID, occurence] for a given word """
def DocsFromWord(word):
    return dictInverse[word]