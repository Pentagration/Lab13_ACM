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
    noun(wordlist)                  #index 0
    verb(wordlist)                  #index 1
    adverb(wordlist)                #index 2
    adjective(wordlist)             #index 3
    words={'noun':wordlist[0],'verb':wordlist[1],'adverb':wordlist[2],'adjective':wordlist[3]}

    for line in file:
        for key in words:
            line=line.replace(key,words[key])
        print line
            
    file.close()
        
madlib()
