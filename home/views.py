from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def credits(request):
    content = "Nicky\nMama"
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {"news": [
        "mama now has a news page!",
        "mama has its first page"
    ]}
    return render(request, "news.html", data)
