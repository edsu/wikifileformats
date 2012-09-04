wikifileformats
===============

My playground for working with articles about file formats on Wikipedia. 

### articles.py

This script will output wikipedia articles that are in the Computer file 
formats category. If you pass it an integer it will descend that many levels
into subcategories. The output for levels 0, 1 and 2 are available here as:

* articles0.txt
* articles1.txt
* articles2.txt
* articles3.txt

You'll notice that as you wander down in the category hierarchy below Computer
file formats the articles become less and less about file formats. That's
because the Wikipedia category system is a graph, not a tree, and it can wander
about a fair bit.
