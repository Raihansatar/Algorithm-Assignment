import plotly.graph_objects as go
import Tries
import RabinKarp
import shutil, os


class Cities:
    # initialize the city object using the textfile
    def __init__(self,text_file_path,name):
        with open(str(text_file_path), encoding="utf8") as myfile:
            data = myfile.read()
            myfile.close()

        self.textfile =str(data)
        self.name = name

    #process the text(remove special char and turn all lowercase) for string matching(remove word list)
    def processCitiesText(self):
        wordstring = self.textfile
        wordstring = wordstring.lower()
        wordlist = wordstring.split()
        self.processedText = " "

        for i in range(len(wordlist)):
            while (wordlist[i][0].isalnum() == False or str(wordlist[i][len(wordlist[i]) - 1]).isalnum() == False):
                if (wordlist[i][0].isalnum() == False):
                    wordlist[i] = wordlist[i][1:]
                if (len(wordlist[i]) == 0):
                    break
                if (str(wordlist[i][len(wordlist[i]) - 1]).isalnum() == False):
                    wordlist[i] = wordlist[i][:len(wordlist[i]) - 1]
                if (len(wordlist[i]) == 0):
                    break
            self.processedText = str(self.processedText) + " " + str(wordlist[i])



    #using RabinKarp Algorithm, remove stopwords.
    def removeStopWords(self, text_file_path):
        with open(str(text_file_path), encoding="utf8") as myfile:
            wordstop=myfile.read().split()
            myfile.close()
            # add space before and after a stopword
            for i in range(len(wordstop)):
                wordstop[i] = " " + wordstop[i] + " "

        rk = RabinKarp
        for i in wordstop:
            indexs = rk.RabinKarp(i, self.processedText, 2, 256)
            shiftcount = 0
            for j in range(len(indexs)):
                shift = indexs[j] - shiftcount
                shiftcount += len(i) - 1
                self.processedText = self.processedText[0:shift + 1:] + self.processedText[shift + len(i)::]

    #remove using TRIES algorithm.
    def removeStopWords_TRIES(self,text_file_path):
        popDictionary= Tries.Tries()
        with open(str(text_file_path), encoding="utf8") as myfile:
            wordstops=myfile.read().split()
            myfile.close()
            for words in wordstops:
                popDictionary.addWord(str(words))

        text = self.processedText.split();
        listOfProcessedText = ""
        i = 0
        while(i<len(text)):
            if(popDictionary.checkForWord(str(text[i]))==False):
                listOfProcessedText = str(listOfProcessedText) + " "+ str(text[i])
            # else:
            #     print(str(text[i])+" - is removed")
            i = i + 1
        self.processedText = listOfProcessedText

    def getFrequency(self):
        Sentence = self.processedText
        dictionary = {}
        lst = Sentence.split()
        for elements in lst:
            if elements in dictionary:
                dictionary[elements] += 1
            else:
                dictionary.update({elements: 1})
        # print the keys and its corresponding values.
        self.elementList = []
        self.elementFrequency = []
        for allKeys in dictionary:
            self.elementList.append(allKeys)
            self.elementFrequency.append(dictionary[allKeys])


    #tries algotithem
    def getPositive_Negative_Neutral_Frequency(self,text_file_path_POSITIVE,text_file_path_NEGATIVE):
        with open(str(text_file_path_POSITIVE), encoding="utf8") as myfile:
            positveList = myfile.read().split(",")
            myfile.close()
        PositiveDictionary = Tries.Tries();
        for words in positveList:
            PositiveDictionary.addWord(str(words))

        with open(str(text_file_path_NEGATIVE), encoding="utf8") as myfile:
            negativeList = myfile.read().split(",")
            myfile.close()
        NegativeDictionary = Tries.Tries();
        for words in negativeList:
            NegativeDictionary.addWord(str(words))

        listOfProcessedTest = self.processedText.split()
        # print(listOfProcessedTest)
        # print(len(listOfProcessedTest))

        PNNdictionary={"Positive":0,
                            "Negative":0,
                            "Neutral":0};

        for i in listOfProcessedTest:
            if(PositiveDictionary.checkForWord(i)):
                PNNdictionary["Positive"] +=1
            elif(NegativeDictionary.checkForWord(i)):
                PNNdictionary["Negative"] +=1
            else:
                PNNdictionary["Neutral"]+=1

        self.alignmentList = []
        self.alignmentFrequency = []
        for allKeys in PNNdictionary:
            self.alignmentList.append(allKeys)
            self.alignmentFrequency.append(PNNdictionary[allKeys])


    def generateGraphCities(self,graph_Name,x_axis, y_axis):
        fig = go.Figure(data=go.Bar(x=x_axis, y=y_axis))
        fig.write_html(str(graph_Name), auto_open=False)

        #move file to the correct place
        if os.path.isdir("html/word_frequency") == False:
            os.makedirs("html/word_frequency");
        shutil.move(str(graph_Name), "html/word_frequency/"+str(graph_Name));



    def generateGraphPNN(self,graph_Name,x_axis, y_axis):
        fig = go.Figure(data=go.Bar(x=x_axis, y=y_axis))
        fig.write_html(str(graph_Name), auto_open=False)

        # move file to the correct place
        if os.path.isdir("html/PPN_frequency") == False:
            os.makedirs("html/PPN_frequency");
        shutil.move(str(graph_Name), "html/PPN_frequency/" + str(graph_Name));

    def generateOverallPNN_Graph(self,cities_list,positive_value_list,negative_value_list,neutral_value_list):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=cities_list,
            y=positive_value_list,
            name='Positive Words',
            marker_color='lightsalmon'
        ))
        fig.add_trace(go.Bar(
            x=cities_list,
            y=negative_value_list,
            name='Negative Words',
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=cities_list,
            y=neutral_value_list,
            name='Neutral Words',
            marker_color='blue'
        ))

        fig.update_layout(barmode='group')
        fig.write_html("Overall_PNN.html", auto_open=False)
        shutil.move("Overall_PNN.html", "html/" + "Overall PNN.html");

    def generateOverallPN_Graph(self,cities_list,positive_value_list,negative_value_list):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=cities_list,
            y=positive_value_list,
            name='Positive Words',
            marker_color='lightsalmon'
        ))
        fig.add_trace(go.Bar(
            x=cities_list,
            y=negative_value_list,
            name='Negative Words',
            marker_color='indianred'
        ))
        fig.update_layout(barmode='group')
        fig.write_html("Overall_PN.html", auto_open=True)
        shutil.move("Overall_PN.html", "html/" + "Overall_PN.html");

    def calculateSentinelValue(self,positive_value_list,negative_value_list,neutral_value_list):
        sv=[]
        for i in range(len(positive_value_list)):
            P = float(positive_value_list[i])
            N = float(negative_value_list[i])
            n = float(neutral_value_list[i])
            sv.append(round(((P-N)/(P+N+n))*100,4))
        return sv

    def sentimentValuePath(self,array):
        y = [1,2,3,4,5,6,7]
        x = array[1:]

        # bubble sort... for y using x(Sentimental Value) as a key
        n = len(x)
        for i in range(n-1):
            for j in range(n-i-1):
                if(x[j]<x[j+1]):
                    x[j],x[j+1]=x[j+1],x[j]
                    y[j],y[j+1]=y[j+1],y[j]

        y=[0]+y+[0]
        return y

