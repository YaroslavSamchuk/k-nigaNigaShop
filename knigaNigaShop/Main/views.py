from django.shortcuts import render

# Create your views here.

def render_main(request):
    return render(request, "Main/main.html")