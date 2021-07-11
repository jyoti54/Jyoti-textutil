# I have created this file -- Jyoti

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def moreofabout(request):
    return render(request, 'moreofabout.html')
def analyze(request):
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charactercount = request.GET.get('charactercount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps =="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
              analyzed = analyzed + char
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] ==" "):
              analyzed = analyzed + char
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charactercount == "on"):
        analyzed = ""
        analyzed = len(djtext)
        params = {'purpose': 'Number of Characters you entered is', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

