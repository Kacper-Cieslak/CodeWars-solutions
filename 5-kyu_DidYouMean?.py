'''
url: https://www.codewars.com/kata/5259510fc76e59579e0009d4/solutions/python

Description:

I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. 
In this kata we want to implement something similar.

 
Your task is to find out, which word from the dictionary is most similar to the entered one. 
Same words are obviously the most similar ones. 
A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed.

Code Examples:

fruits = new Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
fruits.findMostSimilar('strawbery'); // must return "strawberry"
fruits.findMostSimilar('berry'); // must return "cherry"
'''

#Solution:

import difflib

class Dictionary:

    def __init__(self,words):
        self.words=words
        
    def find_most_similar(self,term):
        return difflib.get_close_matches(term, self.words)[0]
