#I have created by own-charvit
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc =request.POST.get('removepunc','off')
    capitalized = request.POST.get('capitalized', 'off')
    newline = request.POST.get('newline','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if capitalized == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Uppercase conversion', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed + char

        params = {'purpose': 'Newline remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremove == "on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed=analyzed + char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char != " " and char != "\n":
                analyzed = analyzed + 1
        params = {'purpose': 'Character counted', 'analyzed_text': analyzed}

    if removepunc == 'on' or capitalized == 'on' or newline == 'on' or spaceremove == 'on' or charcount == 'on':
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('error hai bhai')