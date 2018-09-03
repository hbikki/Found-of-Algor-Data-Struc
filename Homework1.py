longestPosition=0;
smallestPosition=0;
TotalWordsLength=0;
Maxwords=0;
MinWords=9223372036854775807;
paragraph=input("enter text :\n");
paragraphList=paragraph.split('.');
paragraphList.pop();
Position=0;
for i in paragraphList:
    i=i.strip();
    wordList=i.split();
    length=len(wordList)
    if(length > Maxwords):
        longestPosition=Position;
        Maxwords=length;
    if(length < MinWords):
        smallestPosition=Position;
        MinWords=length;
    TotalWordsLength=TotalWordsLength+length;
    Position+=1;
print ("Total No.of words  :  "+str(TotalWordsLength));
print ("Longest Sentence  :  "+ paragraphList[longestPosition].strip());
print ("Smallest Sentence  :  "+paragraphList[smallestPosition].strip());
print ("Before sorting :");
print (paragraphList);
print ("sorting Word Lists:");
for i in paragraphList:
    wordList=i.split();
    wordList.sort();
    print (wordList);
    
    

