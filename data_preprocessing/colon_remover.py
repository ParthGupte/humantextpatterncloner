import os

lineCount = 0
count = 0
underscoreAndSpaceIndex = 20
fileReadList = []

file1 = open(os.path.dirname(__file__) +'\data\WhatsApp_Chat_with_RIP_Gajeebo__Riyal_in_Jageebo.txt', 'r', encoding="utf8")
file2 = open(os.path.dirname(__file__) +'\data\WhatsApp_Chat_with_RIP_RIP__Riyal_is_Inside-Hers.txt', 'r', encoding="utf8")


listOfFiles = [file1, file2]

for fileName in listOfFiles:
    fileLine = fileName.readlines()
    for line in fileLine:
        textVal = line.strip()
        try:
            if textVal[14] == ':':
                textVal = textVal[underscoreAndSpaceIndex:] #removes dash and space after it, deleting date and time
                colonIndex = textVal.index(':')
                textVal = textVal[colonIndex+2:]  #removes name and only text remains
                if textVal != '<Media omitted>':
                    fileReadList.append(textVal)
                    
                    lineCount+=1
        except: 
            continue


#creates a colonless (only till names) text lines
#print(fileReadList)
with open(os.path.dirname(__file__) +'\output\colonLess.txt', 'a', encoding='utf8') as the_file:
    for i in range(0,len(fileReadList)):
        the_file.write(fileReadList[i] + '\n')
