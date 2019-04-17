
def userInput(key):
    word = raw_input("Enter a " + key + " : ")
    return word


def madlib():
    file = open(pickAFile(),'r')
    story = []

    end = 0
    for line in file:
        if '{' in line:
            start = line.find('{', end) + 1 # pass the '{'
            end = line.find('}', start)
            key = line[start : end]
            line=line.replace(key,userInput(key)).replace('\n', '')
        story.append(line)

    for i in story:
        print i