

from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index1.html')

def analyze(request):
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlinesremover=(request.POST.get('newlinesremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    charcounter=(request.POST.get('charcounter','off'))

    if removepunc=='on':
        puncuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in puncuations:
                analyzed=analyzed+char
        param={'purpose':'Remove puncuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',param)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', param)
    if(newlinesremover=='on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', param)

    if (extraspaceremover == 'on'):
        analyzed =" "
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', param)
    if (charcounter == 'on'):
        countchar=0
        for char in djtext:
            if char!=' ':
                countchar+=1
                param = {'purpose': 'count character', 'analyzed_text':countchar}
        # djtext=analyzed
        # return render(request, 'analyze.html', param)

    if(removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and newlinesremover!="on" and charcounter!="on"):
        return HttpResponse('<h1>Please Select Any Oeration To See The Magic</h1>')
    return render(request, 'analyze.html', param)
def contact(request):
    return render(request,'contact.html')






