from django.shortcuts import render


def index(request):
    
    return render(request, 'bug_tracker/index.html')

def about(request):
    return render(request, 'bug_tracker/about.html')
    