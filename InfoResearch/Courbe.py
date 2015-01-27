"""
@authors: CHASSANDE-YOU
"""

import re

def createDictioListDocID_TP(file):
    dictioListDocID_TP = dict()
    starter = ""
    cursor = 0

    for line in file.readlines():
        listLine = line.split(' ')
        # First line or new request
        if (starter == "") | (starter != listLine[0]): 
            starter = listLine[0]
            cursor += 1
            dictioListDocID_TP[cursor] = []
            dictioListDocID_TP[cursor].append(listLine[1])
        # Same request
        else:
            dictioListDocID_TP[cursor].append(listLine[1])

    return dictioListDocID_TP

def createListRequest(file):
    listRequest = []
    cleanLine = ""
    insert = False

    for line in file.readlines():
        if(line.startswith('.W')):
            listRequest.append(cleanLine)
            cleanLine = ""
            insert = True
        elif(line.startswith('.I') | line.startswith('.A') | line.startswith('.B') | line.startswith('.N') | line.startswith('.X') | line.startswith('.T') | line.startswith('.K')):
            insert = False
        elif(insert):
            cleanLine = cleanLine + line.replace(".","").replace(",","").replace("!", "").replace("?", "").replace(";", "").replace("\n", " ")


    return listRequest