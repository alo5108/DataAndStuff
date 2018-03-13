import os

wordcount=[]
linecount = []
average =[]
countword = []
avgword = []

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

PyPara = os.path.join('Resources','paragraph_1.txt')

outputTXT= os.path.join("Resources", "paragraph_1_Rev.txt")

with open(PyPara, newline="") as txtfile:

    para= txtfile.read()
    for word in para.split():
        wordcount.append(word)
    for line in para.split("."):
        if line!="":
            linecount.append(line)
    
    print("Approximate word count:",str(len(wordcount)))
    print("Approximate sentence count:",str(len(linecount)))
    print("Approximate letter count (per word):",str(mean(list(map(len, para.split())))))

    import re
    s= para
    SentList = re.split(r'[?!.]', s)
    Countword = len(re.findall(r'\s', str(SentList)))
    avgword = (Countword)/(len(linecount))
    
    print("Average sentence length (in words):", str(avgword))    

with open(outputTXT, 'w',) as textFile:
    
    textFile.write("Approximate word count = "+ str(len(wordcount)))
    textFile.write("\n" + "Approximate sentence count = "+str(len(linecount)))
    textFile.write("\n"+ "Approximate letter count (per word) = " +str(mean(list(map(len, para.split())))))
    textFile.write("\n"+ "Average sentence length (in words) = " + str(avgword))