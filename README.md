# PageRank Implementation
<p>
This project provides an open source PageRank implementation. The
implementation is a straightforward application of the algorithm
description given in the American Mathematical Society's Feature
Column [How Google Finds Your Needle in the Web's
Haystack](http://www.ams.org/samplings/feature-column/fcarc-pagerank),
by David Austing. It can handle very big hyperlink graphs with
millions of vertices and arcs.
</p>

# Downloading Dependencies:
<p>
Download the zip and you will find the following components in file: 
</p>

<pre>
1) <b><i>src/*</b></i> : Contains the source code and the source srt file(links.srt) which contains millions of links(56MiB compressed, 245 MiB uncompressed).
           a)pageRank.py
           b)links.srt
              
   2) <b><i>inlinks.txt</b></i> : A text file with the top 100 pages by number of inlinks, with the title (source URL), rank (1..100), and inlink count on each line.
   3) <b><i>pagerank.txt</b></i> :A text file with the top 100 pages by their PageRank, with title (source URL), rank (1..100) and score on each line.
</pre>

   


# Building the Code:
To build the code, simply run the pageRank.py in the terminal using the following statement:
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>            "python3"          "/Users/rupinmehra/pageRank/src/pageRank.py"          newlinks.srt
                          ( location of pageRank.py in the particular system )     (file to implement)
</code></pre></div></div>


Input Format:
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> Source_Page_Name1 '\t' Target_Page_Name1 '\n'
 Source_Page_Name1 '\t' Target_Page_Name2 '\n'
 Source_Page_Name2 '\t' Target_Page_Name3 '\n'
 ...
</code></pre></div></div>

We are given the values of lamda and tau used to implement the process:

Tau(0.005): Based on random category assignment. It measures the percentage improvement in predictability of the dependent variable given the value of other variables.

Lamda(0.20): Lamda is a measure of proportional reduction in error in cross tabulation analysis. 
<div>
1) <b><i>pageRank.py</b></i> : The file imports the test file and processes the link. A link is represented as a pair (x, y) where x and y 
                     are the source and destination pages respectively. Dangling links are assumed to be removed. 
                     Ranksinks accumulate pagerank but do not distribute it. Also, we have assumed that pages link to all other pages in the collection.
<pre>
      a) <b><i>Inlinks</b></i>:
                To Web page x, an inlink is a URL of another Web page which contains a link pointing to x.
                Makes the use of standard libraries in Python. (https://docs.python.org/3/library/).
                Counter() creates a hash-map for the data container invoked with it which is very useful than by manual processing of elements. 
                Counts the outgoing links for each page and returns the top 100 links in terms of inlinks in 
                descending order.
</pre>  
<pre>
      b) <b><i>Page Rank</b></i>:
                We start of by calculating the probabilities for every function such that they are equally likely 
                to be selected. Then we calculate the uique probabilty of each page. (lambda / probabilty of random selection).
                Then we calculate the sum of probabilities page by page and apply the R operation and find it's rank until the value of R converges.
                We write these values into the output file(pagerank.txt) and return it.  
</pre>
</div>
   
# Running the Code:

The src file import the input text files and running the code will return the output file in the main directory. 
The test file can be ran inside the src to check the output.
