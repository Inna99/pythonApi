from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "index.html", context={"now": now})


def profile(request):
    username = request.user.username
    return render(request, "profile.html", context={"username": "Hello " + username})
