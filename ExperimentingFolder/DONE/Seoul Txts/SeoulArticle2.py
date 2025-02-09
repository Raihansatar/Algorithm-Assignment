wordstring="South Korean economy grew 2.7 percent in 2018 — the slowest pace in six years"
wordstring+="Published Mon, Jan 21 20198:22 PM ESTUpdated Mon, Jan 21 20198:30 PM EST"
wordstring+="Key Points"
wordstring+="South Korea’s economy grew 3.1 percent year-on-year in the final three months of 2018, beating the 2.8 percent estimated by economists in a Reuters poll."
wordstring+="The quarterly GDP growth was helped by a jump in government spending."
wordstring+="However, the 2.7 percent expansion for the entire 2018 was the slowest in six years."
wordstring+="South Korea’s economy expanded at the fastest pace in three quarters in the last three months of 2018 as a jump in government spending juiced up construction and investment, though weak exports cast a cloud over the outlook for growth."
wordstring+="Gross domestic product increased by a seasonally adjusted 1 percent in the fourth quarter from three months earlier, the Bank of Korea’s advance estimates showed on Tuesday, beating the median forecast of 0.6 percent in a Reuters survey."
wordstring+="The annual pace accelerated to 3.1 percent, handily outpacing 2.0 percent in the third quarter and marking the fastest expansion in five quarters."
wordstring+="The economy rode a surge in government spending, which increased by 3.1 percent on-quarter for its biggest rise in almost nine years and helped boost construction and capital investment."
wordstring+="\“Increased fiscal spending towards the year end has cushioned the blow to exports, as shipments of chips and electronic products are falling,\” a central bank official said."
wordstring+="Construction investment climbed 1.2 percent in the fourth quarter while capital investment jumped 3.8 percent, the sharpest increase in six quarters."
wordstring+="Private consumption expanded at double the pace seen in the third quarter with a 1 percent growth rate."
wordstring+="Exports, however, declined 2.2 percent on-quarter and remained the biggest risk for South Korea’s trade-reliant economy this year."
wordstring+="Indeed, the full year told a story of increasing strain across the economy. Growth was 2.7 percent for the whole of 2018, the slowest expansion in six years but matching the 2.7 percent growth projected by the central bank."
wordstring+="Investor worry a slowdown in the Chinese economy and the Sino-U.S. trade war could severely dent global growth and demand for key South Korean exports items including memory chips and petrochemical products."
wordstring+="Growing signs of weakness in China — which has generated nearly a third of global growth in recent years — are fueling anxiety about risks to the world economy and are weighing on profits for firms ranging from Apple to big car-makers. Last year, China’s economy grew an annual 6.6 percent, the slowest pace in almost three decades, hurt by the trade war and slackening domestic demand."
wordstring+="December exports unexpectedly slipped as shipments to China, South Korea’s biggest export market, declined 14 percent on-year, the fastest fall in more than two years."
wordstring+="The pressure on the South Korean economy is expected to persist over this year, and likely keep the central bank sidelined after it raised rates in November mainly to contain a boom in parts of the nation’s property market."
wordstring+="The Bank of Korea holds its first meeting for the year on Thursday"

wordlist= wordstring.split()
wordfreq=[]

for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
