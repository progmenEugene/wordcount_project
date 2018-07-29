from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	wordcountdict = {}
	for words in wordlist:
		if words in wordcountdict:
			#increase
			wordcountdict[words] += 1
		else:
			#add to the dict
			wordcountdict[words] = 1
	sortedwords = sorted(wordcountdict.items(), key = operator.itemgetter(1), reverse = True)
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})