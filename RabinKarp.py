def RabinKarp(pattern, text, prime, numOfChar):
    index=[]
    m = len(pattern)
    n = len(text)
    pHmap = 0
    tHmap = 0
    i=0
    j=0

    #calculating the hmap of pattern and the first comparison of text
    for i in range(m):
        pHmap = (numOfChar*pHmap + ord(pattern[i]))%prime
        tHmap = (numOfChar*tHmap +ord(text[i]))%prime


    #shift and compare between the 2 hmap
    for i in range(n-m+1):
        #check if hmap is same
        if pHmap==tHmap:
            for j in range(m):

                #compare the pattern and text
                if pattern[j]!=text[j+i]:
                    #skipping the counter thus exit the loop
                    break

                #counter to count if the number of same char
                j+=1
                #when the j is same as m --> same sequence
                if j==m:
                    # print("Pattern found at index " + str(i))
                    index.append(i)

        #if still have char in text to search
        if i < n-m:
            # 1. remove the value at i
            # 2. adding the next value at i+m for the hmap
            # pow(numOfChar,m-1) is h (helps with the shifting)
            tHmap = ((numOfChar*(tHmap-ord(text[i])*pow(numOfChar,m-1))) + ord(text[i+m]))%prime

            #make sure it is +ve
            if tHmap < 0:
                tHmap = tHmap+prime

    return index
#
# # RabinKarp("fun","algorithmisfun",17,10)
#
#





