wordstring="South Korea's economy grew at decade-low pace in 2019"
wordstring+="Despite higher government spending, the country's economy was dragged down by weaker exports last year."
wordstring+="South Korea's central bank warned that a deadly new virus spreading rapidly from Wuhan, China could hurt consumer spending [File: Heo Ran/Reuters]"
wordstring+="Sagging exports and global trade tensions pulled South Korea's annual growth rate last year to its lowest level since 2009, but a surge in government spending may have given the economy a boost in the last three months of 2019."
wordstring+="The slowdown comes as President Moon Jae-in's administration increases fiscal spending and as the Bank of Korea (BOK) considers further stimulus to shield the economy from a global slowdown."
wordstring+="More:"
wordstring+="South Korea's Moon vows 'endless' property price curbs "
wordstring+="South Korea inequality: Youth fed up with wealth gap"
wordstring+="South Korea no longer wants to be treated as 'developing country"
wordstring+="The gross domestic product (GDP) increased by a seasonally adjusted 1.2 percent in the fourth quarter of 2019 compared with the previous three months, the BOK said on Wednesday."
wordstring+="It was the fastest expansion since the third quarter of 2017 and outperformed the median estimate of 0.8 percent in a survey by Reuters news agency."
wordstring+="\"Government spending definitely was a boost as exports was a drag,\" said Park Chong-hoon, an economist at Standard Chartered Bank in Seoul. \"The prospect for exports is better this year with the US-China signing of the trade deal, and as China continues with its expansionary fiscal policies.\""
wordstring+="Robust government spending on public infrastructure combined with better private consumption improved growth in the fourth quarter, but that did little to help exports, which made no contribution to the 1.2 percent expansion."
wordstring+="In the fourth quarter, private consumption increased 0.7 percent from three months earlier while construction investment jumped 6.3 percent."
wordstring+="For the whole of 2019, the economy grew by 2 percent, the slowest pace in 10 years and matching the central bank's projection."
wordstring+="\"Of the 2 percent, the net government contribution to growth came to 1.5 percentage points, the biggest portion since 2009 but that didn't change the fact that it was a hard year for Korea in terms of exports,\" a central bank official said."
wordstring+="In a press briefing held after the GDP data release, another BOK official said the outbreak of a virus from central China has emerged as a fresh risk that could hurt consumer spending."
wordstring+="\"With the case of the Middle East Respiratory Syndrome (MERS), people didn't go out much and travelled less, so spreading of the new virus may shrink consumption in that regard,\" Park Yang-su, a director general at the BOK, said in response to a question about the virus."
wordstring+="South Korea in 2015 drew up a supplementary budget to help the economy cope with the effects of the outbreak of the MERS."
wordstring+="The virus in China, originating in the central city of Wuhan at the end of last year, has spread to Beijing, Shanghai and elsewhere, with cases also confirmed in the United States, Thailand, South Korea, Japan and Taiwan."

wordlist= wordstring.split()
wordfreq=[]

for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))