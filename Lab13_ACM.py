# Lab 13
# Adam Colin Marcus

def noun(list):
    word = raw_input("Enter a noun: ")
    list.append(word)
    return list

def verb(list):
    word = raw_input("Enter a verb: ")
    list.append(word)
    return list

def adverb(list):
    word = raw_input("Enter an adverb: ")
    list.append(word)
    return list

def adjective(list):
    word = raw_input("Enter an adjective: ")
    list.append(word)
    return list

def madlib():
    file=open(pickAFile(),'r') 
    wordlist = []
    words={'noun':noun(wordlist),'verb':verb(wordlist),'adverb':adverb(wordlist),'adjective':adjective(wordlist)}

    for line in file:
        for key in words:
            line=line.replace(key,words[key])
        print line
            
    file.close()
        
madlib()
