import RabinKarp

with open ("../../textfile/KualaLumpur.txt", "r") as myfile:
    data=myfile.read()
    print(str(data))

wordstring = str(data)
wordstring = wordstring.lower()
wordlist = wordstring.split()
finalTEXT = " "

for i in range(len(wordlist)):
    if wordlist[i].endswith("\""):
        wordlist[i] = wordlist[i].replace("\"", "")
    if wordlist[i].startswith("\""):
        wordlist[i] = wordlist[i].replace("\"", "")
    if wordlist[i].endswith(")"):
        wordlist[i] = wordlist[i].replace(")", "")
    if wordlist[i].startswith("("):
        wordlist[i] = wordlist[i].replace("(", "")
    if wordlist[i].endswith("."):
        wordlist[i]=wordlist[i].replace(".","")
    if wordlist[i].endswith(","):
        wordlist[i] = wordlist[i].replace(",", "")
    if wordlist[i].endswith(":"):
        wordlist[i] = wordlist[i].replace(":", "")
    finalTEXT = finalTEXT + wordlist[i] + " "


# print("\n\n")
# print(wordlist)
print("\n\n")
# print(finalTEXT)

with open ("../../textfile/stopwords_DefaultEnglish.txt", "r") as myfile:
    wordstop=myfile.read().split()


for i in range(len(wordstop)):
    wordstop[i] = " "+wordstop[i]+" "


# print(wordstop)

rk = RabinKarp

for i in wordstop:
    # print(i)
    indexs = rk.RabinKarp(i,finalTEXT,2,256)
    # print(indexs)
    shiftcount=0
    for j in range(len(indexs)):

        shift = indexs[j]-shiftcount
        shiftcount += len(i)-1
        finalTEXT = finalTEXT[0:shift + 1:] + finalTEXT[shift+len(i)::]
    #     print(finalTEXT)
    #
    # print("\n")
    # print("----------------------------------")
print(finalTEXT)



# --------------------------------------------------------------------------------------------------------------------------------




Sentence = finalTEXT

dictionary = {}

lst = Sentence.split()


for elements in lst:
    if elements in dictionary:
        dictionary[elements] += 1

    else:
        dictionary.update({elements: 1})

# print the keys and its corresponding values.
for allKeys in dictionary:
    print(allKeys)
    print(dictionary[allKeys])
