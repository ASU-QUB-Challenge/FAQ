#TODO: Add import statements if needed
import nltk
#import sklearn
#import ...

continueCoversation = True
solutionFound = False
count = 1

def Diagnose(input, responseNum):
    initString = "ChatBot #:" + str(responseNum) + " >>> "
    #tokens = nltk.tokenize.word_tokenize(input)
    #pos = nltk.pos_tag(tokens)
    #findName = True
    #while findName:
    
    response = "Not Implemented"
    return initString + response;


while continueCoversation:
    userInput = raw_input("Agent >>> ")
    print(Diagnose(userInput, count))
    count = count + 1
    #TODO: Set solutionFound to True, once you have determined that you have satisfied the user request
    
    if solutionFound:
        continueCoversation = False

print("I have determined that I've satisfied your request. Thank you for using ChatBot. Have a nice day!")