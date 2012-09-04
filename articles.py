#!/usr/bin/env python

import sys

"""
Outputs Wikipedia articles that are in the Computer file formats category.
"""

import json
import requests

def main(depth=0):
    seen = set()
    for cat in subcategories("Category:Computer_file_formats", max_depth=depth):
        for article in category_articles(cat):
            if not article in seen:
                seen.add(article)
                print article.encode('utf-8')

def category_articles(category):
    """returns Wikipedia articles in a given category.
    """
    url = "https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmnamespace=0&cmlimit=500&cmtitle=%s&format=json" % category
    for cat in get_json(url)['query']['categorymembers']:
        yield cat['title']

def subcategories(category, seen=None, depth=0, max_depth=5):
    """generator for returning all subcategories of a given category
    """
    if not seen: 
        seen = set()

    # base case for recursion
    if category in seen:
        return
    seen.add(category)

    # don't wander too far, Wikipedia's categories are a graph, not a tree
    if depth > max_depth:
        return

    # get sub-categories for the category
    url = "https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmnamespace=14&cmlimit=500&cmtitle=%s&format=json" % category
    for cat in get_json(url)['query']['categorymembers']:
        cat_title = cat['title']
    
        if not cat_title in seen:
            yield cat_title
            for subcat in subcategories(cat_title, seen=seen, depth=depth + 1, max_depth=max_depth):
                yield subcat

def get_json(url):
    r = requests.get(url, headers={"user-agent": "fileformatsbot"})
    return json.loads(r.content)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        depth = 0
    else:
        depth = int(sys.argv[1])
    main(depth)
