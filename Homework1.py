longestPosition=0;
smallestPosition=0;
TotalWordsLength=0;
Maxwords=0;
MinWords=9223372036854775807;
paragraph=input("enter text :\n");
paragraphList=paragraph.split('.');
print ("=======================================================================");
print ("Total No.of sentences before fix :  "+str(len(paragraphList)));
print ("=======================================================================");
print ("Last sentences before fix:  "+paragraphList[len(paragraphList)-1]);
print ("=======================================================================");
paragraphList.pop();
print ("Total No.of sentences after fix :  "+str(len(paragraphList)));
print ("=======================================================================");
print ("Last sentences after fix:  "+paragraphList[len(paragraphList)-1]);
print ("=======================================================================");
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
print ("=======================================================================");
print ("Longest Sentence  :  "+ paragraphList[longestPosition].strip());
print ("=======================================================================");
print ("Smallest Sentence  :  "+paragraphList[smallestPosition].strip());
print ("=======================================================================");
allWordsList=paragraph.split(' ');
print ("Before sorting :");
print (allWordsList);
print ("=======================================================================");
allWordsList.sort();
print ("sorting Word Lists:");
print (allWordsList);
print ("=======================================================================");