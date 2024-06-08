from django.http import HttpRequest, HttpResponse

def index(request):
    return HttpResponse("hello")
def about(request):
    return HttpResponse("word")
