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
    wordlist = []
    stringlist = []
    #string1 = "This is a test for a noun: "
    #string2 = "This is a test for a verb: "
    #string3 = "This is a test for a adverb: "
    #string4 = "This is a test for a adjective: "
    stringlist.append("This is a test for a noun: ")
    stringlist.append("This is a test for a verb: ")
    stringlist.append("This is a test for a adverb: ")
    stringlist.append("This is a test for a adjective: ")
    noun(wordlist)
    verb(wordlist)
    adverb(wordlist)
    adjective(wordlist)

    #print string1 + wordlist[0]
    #print string2 + wordlist[1]
    #print string3 + wordlist[2]
    #print string4 + wordlist[3]
    for i in range(0, len(wordlist)):
        print stringlist[i] + wordlist[i]
