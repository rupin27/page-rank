#PageRank Implementation

This project provides an open source PageRank implementation. The
implementation is a straightforward application of the algorithm
description given in the American Mathematical Society's Feature
Column [How Google Finds Your Needle in the Web's
Haystack](http://www.ams.org/samplings/feature-column/fcarc-pagerank),
by David Austing. It can handle very big hyperlink graphs with
millions of vertices and arcs.

#DOWNLOADING DEPENDENCIES:

Download the zip and you will find the following components in file: 
   1) src/* : Contains the source code, source srt file(links.srt), and a test srt file to check implementation.
               a)pageRank.py
               b)links.srt
               c)newlinks.srt(test file)

   2) inlinks.txt : A text file with the top 100 pages by number of inlinks, with the title (source URL), rank (1..100), and inlink count on each line.
   3) pagerank.txt :A text file with the top 100 pages by their PageRank, with title (source URL), rank (1..100) and score on each line.

#BUILDING THE CODE:
To build the code, simply run the pageRank.py in the terminal using the following statement:

            "python3"          "/Users/rupinmehra/pageRank/src/pageRank.py"          newlinks.srt
                          ( location of pageRank.py in the particular system )     (file to implement)
Input Format:
            Source_Page_Name1 '\t' Target_Page_Name1 '\n'
            Source_Page_Name1 '\t' Target_Page_Name2 '\n'
            Source_Page_Name2 '\t' Target_Page_Name3 '\n'
            ...
We are given the values of lamda and tau used to implement the process:

Tau(0.005): Based on random category assignment. It measures the percentage improvement in predictability of the dependent variable given the value of other variables.

Lamda(0.20): Lamda is a measure of proportional reduction in error in cross tabulation analysis. 

1) pageRank.py : The file imports the test file and processes the link. A link is represented as a pair (x, y) where x and y 
                     are the source and destination pages respectively. Dangling links are assumed to be removed. 
                     Ranksinks accumulate pagerank but do not distribute it. Also, we have assumed that pages link to all other pages in the collection.

      a) Inlinks:
                To Web page x, an inlink is a URL of another Web page which contains a link pointing to x.
                Makes the use of standard libraries in Python. (https://docs.python.org/3/library/).
                Counter() creates a hash-map for the data container invoked with it which is very useful than by manual processing of elements. 
                Counts the outgoing links for each page and returns the top 100 links in terms of inlinks in 
                descending order.

      b) Page Rank:
                We start of by calculating the probabilities for every function such that they are equally likely 
                to be selected. Then we calculate the uique probabilty of each page. (lambda / probabilty of random selection).
                Then we calculate the sum of probabilities page by page and apply the R operation and find it's rank until the value of R converges.
                We write these values into the output file(pagerank.txt) and return it.    

RUNNING THE CODE:

The src file import the input text files and running the code will return the output file in the main directory. 
The test file can be ran inside the src to check the output.
