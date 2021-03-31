from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "index.html", {"now": now})


def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Uncnown"
    print(request.user)
    return render(request, "profile.html", {"username": username})


def languages(request):
    return render(request, "languages.html")
