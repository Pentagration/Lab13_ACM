# Colin Reed, Marcus Gonzalez, Adam Houser
# CST 205 Spring 2019
# Lab 14

def userInput(key):
    #presents user with a word type to replace and return user's input
    word = raw_input("Enter a " + key + " : ")
    return word


def madlib():
    # reads a file, looks for key words in { } to replace MadLib style
    file = open(pickAFile(),'r')
    story = []

    end = 0
    for line in file:
        if '{' in line:     # checks line for replaceable word
            start = line.find('{') + 1 # pass the '{'
            end = line.find('}')
            key = line[start : end]
            line=line.replace(key,userInput(key)).replace('\n', '')
        story.append(line)  # appends line to list for printing

    for i in story:
        print i
