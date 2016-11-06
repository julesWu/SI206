#name: Julia Wu
#UMID: 38632603
#Unique name: shuyue
#References: madlibgenerator.py, nltk book website

import nltk
import random

# import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print("START*******")

debug = False

sense = nltk.corpus.gutenberg.raw('austen-sense.txt')
#print (sense[0:150])
tokens = nltk.word_tokenize(sense)
print("TOKENS")
print(tokens[0:150])
tagged_tokens = nltk.pos_tag(tokens[:150]) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)
#if debug:
	#print ("First few tagged tokens are:")
	#for tup in tagged_tokens[:5]:
		#print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "VBD": "a past-tense verb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "VBD":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")
