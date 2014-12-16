"""
@authors: CHASSANDE-YOU
"""

""" Return a boolean (0 or 1) array from two given array merging them with OR rule """     
def PushArrayOr(array1, array2):
    arrayReturned = [0 for i in range(len(array1))]
    for i in range (len(array1)):
        arrayReturned[i] =  max(array1[i],array2[i])
    return arrayReturned     
            
""" Return a boolean (0 or 1) array from two given array merging them with AND rule """  
def PushArrayAnd(array1, array2):
    arrayReturned = [0 for i in range(len(array1))]
    for i in range (len(array1)):
        arrayReturned[i] =  min(array1[i],array2[i])
    return arrayReturned

""" Return a list of docID containing the words in the request (request pattern: (A OR B OR NOT C) AND (D OR E)...) """
def BooleanRequest(request, dictioWord, common_words):
    listDocID = list()
    dictioLength = len(dictioWord)

    # Array Global for AND
    arrayGlobal = [1 for i in range(dictioLength)]

    # Parsage string with AND (each substring has a (A OR B OR NOT C) pattern)
    substrings = request.split(" AND ")

    # Parsage substrings with OR (each word has a "(A" or "B" or "NOT C" or "D)" pattern)
    for substring in substrings:
                
        # Array Partiel for OR
        arrayPartiel = [0 for i in range(dictioLength)] 

        words = substring.split(" OR ")
        for word in words:
            # Remove "(", ")" (each word has a "A" or "NOT B" pattern)
            wordClean = word.replace("(", "").replace(")", "")
            
            # Array Local for NOT
            arrayLocal = [0 for i in range(dictioLength)]
            notCondition = 1
            if(wordClean.startswith("NOT")):
                notCondition = 0
            
            # Remove "NOT" and " " (each word has a "A" pattern)
            wordClean = wordClean.replace("NOT", "").replace(" ","").lower()
            if(wordClean in dictioWord):
                for i in dictioWord[wordClean]:
                    arrayLocal[i] = notCondition

            #ArrayLocal push into ArrayPartiel with OR condition 
            arrayPartiel = PushArrayOr(arrayLocal, arrayPartiel)
        
        #ArrayPartiel push into ArrayGLobal with AND condition
        arrayGlobal = PushArrayAnd(arrayPartiel, arrayGlobal)

    for i in range(dictioLength):
        if(arrayGlobal[i] == 1):
            listDocID.append(i)

    return listDocID  

#TODO: add filter on BooleanRequest for common_words