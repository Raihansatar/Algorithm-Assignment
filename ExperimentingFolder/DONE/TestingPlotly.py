import plotly.graph_objects as go
import RabinKarp

with open ("../../textfile/Taipei.txt", encoding="utf8") as myfile:
    data=myfile.read()

wordstring = str(data)
wordstring = wordstring.lower()
wordlist = wordstring.split()
finalTEXT = " "

for i in range(len(wordlist)):
    while(wordlist[i][0].isalnum()==False or str(wordlist[i][len(wordlist[i])-1]).isalnum()==False):
        if(wordlist[i][0].isalnum()==False):
            wordlist[i] = wordlist[i][1:]
        if(len(wordlist[i])==0):
            break
        if(str(wordlist[i][len(wordlist[i])-1]).isalnum()==False):
            wordlist[i] = wordlist[i][:len(wordlist[i])-1]
    finalTEXT = str(finalTEXT) +" "+ str(wordlist[i])

print("\n\n")
print(finalTEXT)
print(wordlist)

with open ("../../textfile/stopwords_DefaultEnglish.txt", "r") as myfile:
    wordstop=myfile.read().split()
for i in range(len(wordstop)):
    wordstop[i] = " "+wordstop[i]+" "

rk = RabinKarp
for i in wordstop:
    indexs = rk.RabinKarp(i,finalTEXT,2,256)
    shiftcount=0
    for j in range(len(indexs)):
        shift = indexs[j]-shiftcount
        shiftcount += len(i)-1
        finalTEXT = finalTEXT[0:shift + 1:] + finalTEXT[shift+len(i)::]

Sentence = finalTEXT
dictionary = {}
lst = Sentence.split()

for elements in lst:
    if elements in dictionary:
        dictionary[elements] += 1

    else:
        dictionary.update({elements: 1})

# print the keys and its corresponding values.
elementList = []
elementFrequency = []
for allKeys in dictionary:
    elementList.append(allKeys)
    elementFrequency.append(dictionary[allKeys])

print(elementList)
print(elementFrequency)




fig = go.Figure(data=go.Bar(x=elementList, y=elementFrequency))
fig.write_html('first_figure.html', auto_open=True)





















