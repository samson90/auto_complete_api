import pandas

def predictWords(phrase, one_tdm, two_tdm, three_tdm):
	phrase = phrase.lower()
	terms = phrase.split(" ")
	bFound = False
	words = []
	freq = []
	while not bFound and len(terms) > 0:
		try: 
			if len(terms) > 1: 
				#search for predicted word based on previous two terms
				sub = three_tdm.loc[terms[len(terms)-2], terms[len(terms)-1]]
				sub = sub.sort('freq', ascending=False)
			else:
				# search for predicted word based on previous term
				sub = two_tdm.loc[terms[len(terms)-1]]
				sub = sub.sort('freq', ascending=False)
				
			words = sub[0:3]['n0']
			bFound = True
			freq = sub[0:3]['freq']
		except KeyError: # couldn't find any matching words
			terms = []
	if not bFound:
		words = one_tdm['n0']
		freq = one_tdm['freq']
	return (words, freq)