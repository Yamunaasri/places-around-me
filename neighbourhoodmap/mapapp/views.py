from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request, "mapapp/map.html")

def rakkitheatre(request):
    return render(request, "mapapp/rakkitheatre.html")

def ponnusupermarket(request):
    return render(request, "mapapp/ponnusupermarket.html")

def midnightdhaba(request):
    return render(request, "mapapp/midnightdhaba.html")

def bigboss(request):
    return render(request, "mapapp/bigboss.html")

def corporationpark(request):
    return render(request, "mapapp/corporationpark.html")