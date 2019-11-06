from django.shortcuts import render

# Create your views here.

def index(req):
    context = {

    }
    return render(req, "index.html", context=context) 
    # index.html을 그릴 때 context에 넘겨줄 값

def single(req):
    context = {

    }

    return render(req, "single.html", context=context)
