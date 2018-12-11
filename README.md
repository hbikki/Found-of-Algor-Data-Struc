
===================================================================================================================================
Project :

Sentiment analysis in Twitter for top5 test cricket players

=====================================================================
This is the first programming assignment.  It is due in class on Wednesday, September 5.

You must do this on your own.  If you have questions, it is fine to post them on our Piazza page.  It is not ok to ask "How do I do ....".  You could ask for pointers to help with some aspect of the problem, or clarification of anything that is not clear.  If you have a question about possible features of the test data, you may ask.

Upload your .py file here.  It will be tested with data that is not what you used, so be sure to make your code independent of your test data.


Here are the instructions:

=====================================================================
Homework 1:  Some text manipulation

 Write a program to do the following:

 Input a paragraph of at least 3 sentences, preferably more. (Copy a paragraph or two from a news article or a web page about some subject of interest. )

In our first class, we split the sentence into words by splitting on the blank space between words.  That is the default for split.  You can also split on other characters by naming them.  Look it up. 

Separate your input into sentences.  For now, just separate on the ‘.’ that ends most sentences.

 Print out the following, with an appropriate label for each and reasonable spacing:

How many sentences were there?
Be careful.  Explore a bit.  Check the answer.
What is the last sentence?  Is this a problem? 
How would you fix it?
How many total words in all the sentences? (Report the number of words found in the list.  It is not necessary to remove non-words yet.)
Print out the longest sentence (longest in words, not characters.)
Print out the shortest sentence
Sort the words in the list.
Print out the sorted list of words.
Take a look at the sorted list of words to see what the default processes consider a word.
Test your program carefully.  Realize that when it is tested, the input used will be different from yours.  Thus, you must not allow your program to be specific to the particular paragraph that you read.

 

NOTE, PLEASE: Print out only what is asked for.  If you have extra print statements used for debugging, comment them out in the final code. The output must be just what is asked for.

====================================================================================================
Assignment
Program 2: Exploring text
From NLTK book, Chapter 1:

◑ Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].

Ending in ize
Containing the letter z
Containing the sequence of letters pt
Having all lowercase letters except for an initial capital (i.e., titlecase)
Do this and write the results to a file.  Upload your python code and also the output file.
====================================================================================================
Assignment
Homework 3: NLTK documents
UPDATE TO ASSIGNMENT: 

The limited number of concordance records does not allow a complete review of the text, in most cases.

 

To do the programming assignment, please use the sentence tokenizer and use that to look at each sentence, see if However appears at the beginning, and then see how it is used.  Think about how you will distinguish one kind of use from the other.

 

Here is an example from a web site of how to use the sentence tokenizer:

    >>> from nltk.tokenize import sent_tokenize, word_tokenize
    >>> sent_tokenize(s)
    ['Good muffins cost $3.88\nin New York.', 'Please buy me\ntwo of them.', 'Thanks.']
    >>> [word_tokenize(t) for t in sent_tokenize(s)]
    [['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.'],
    ['Please', 'buy', 'me', 'two', 'of', 'them', '.'], ['Thanks', '.']]
The site is https://www.nltk.org/_modules/nltk/tokenize.html


Another site: https://textminingonline.com/dive-into-nltk-part-ii-sentence-tokenize-and-word-tokenize

Example: 

>>> text = “this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn.”
>>> from nltk.tokenize import sent_tokenize
>>> sent_tokenize_list = sent_tokenize(text)
>>> len(sent_tokenize_list)
5
>>> sent_tokenize_list
[“this’s a sent tokenize test.”, ‘this is sent two.’, ‘is this sent three?’, ‘sent 4 is cool!’, “Now it’s your turn.”]
>>>



From NLTK book exercises, chapter 2:     According to Strunk and White's Elements of Style,     the word however, used at the start of a sentence, means     "in whatever way" or "to whatever extent", and not     "nevertheless". They give this example of correct usage:     However you advise him, he will probably do as he thinks best.     (http://www.bartleby.com/141/strunk3.html)     Use the concordance tool to study actual usage of     this word in the various texts we have been considering. 

Specifically, do this for all the files in the Gutenberg collection. DO NOT TYPE IN THE NAME OF EACH OF THE BOOKS.  Loop through them.  Include a separate text file in which you describe what you see and what you can conclude.

Then, choose one of the categories of the Brown corpus and repeat the exercise. You can make that part of the same program, or do a separate one.  Your discussion can be part of the same text file or a separate one.

Bonus: Loop through all the files in all the categories of the Brown corpus.

As always, your program must be well designed and must include good documentation and meaningful variable names.  If using a function will make your program easier to read and understand, then use one. 

====================================================================================================
Assignment
Program 4: Reading level
Download text from two web sites and analyze the reading level of each. You may use the ARI (Automated Readability Index) described in Exercise 28 of Chapter 3, or look up and use a different scoring technique.  If you use a different one, be sure to describe it in your documentation.

Use websites that have a lot of text, perhaps news sites, or you could use a wikipedia page for one of the sites.  Pick sites you expect to have different scores.  Use just one page  from each site to do the analysis 


For your output, print the url of the web page you used and its reading score.  If the page has a title, print that also.
====================================================================================================
Assignment
Program 5: Program - Regular Expressions
Exercise 38, Chapter 3:

An interesting challenge for tokenization is words that have been split across a line-break. E.g. if long-term is split, then we have the string long-\nterm.

Write a regular expression that identifies words that are hyphenated at a line-break. The expression will need to include the \n character.
Use re.sub() to remove the \n character from these words.
How might you identify words that should not remain hyphenated once the newline is removed, e.g. 'encyclo-\npedia'?
Make a good test file and upload that along with your program.  Your test file should exercise your program well.  The TA will test your program with your test file, and with another test file that you do not see.
====================================================================================================
Assignment
Program 6: Baby Names
Use the Baby Names data.

 Write a program to output the following information, clearly labeled:

What was the most common boy’s name in 1900?
Accept a name and gender as an input from the console
output the year in which that was the most common name for that gender.
Plot the changing popularity of that name over the years from 1880 to the present
Accept a year as input from the console
Print out the 25 most popular girls names and the 25 most popular boys names for that year
====================================================================================================
Assignment
Program 6: Mining the Movie Reviews Data
The program specification will be developed in class
====================================================================================================
Assignment
Program 7 - Twitter API Exploration
Submit the classwork of November 7th, 2018


