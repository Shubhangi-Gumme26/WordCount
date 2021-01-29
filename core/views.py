import operator
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def count(request):
    countdata = request.POST.get('fulltextarea')
    word_data = countdata.split()
    word_data_len = len(word_data)

    worddict = {}
    for word in word_data:
        if word in worddict:
            worddict[word]=worddict[word]+1
        else:
            worddict[word]=1
    sorted_list = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'core/count.html',{'FullText':countdata, 'CountWords':word_data_len, 'WordDict':sorted_list})