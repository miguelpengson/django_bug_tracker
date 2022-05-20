from django.http import HttpResponse

# first view
def index(request):
    return HttpResponse('Hello, this is the landing page of the bugtracking app!')