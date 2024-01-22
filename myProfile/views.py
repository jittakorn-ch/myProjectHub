from django.http import HttpResponse

def index(request):
    return HttpResponse('Hollo, My Project!!!')
