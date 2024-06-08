from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("word")
def removepunc(request):
    text = request.GET.get('text', 'default')
    punc=request.GET.get('removepunc', 'default')

    if punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        text=analyzed



    params ={'text': text, 'punc':punc}
    return render(request, 'removepunc.html',params)
