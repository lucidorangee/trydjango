from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_context = {
        "title" : "This is about me",
        "my_number" : 123,
        "my_list" : ["Person A", "Person B", "Person C"],
        "my_html" : "<h1>Testing MyHTML Context</h1>"
    }
    return render(request, "about.html", my_context)