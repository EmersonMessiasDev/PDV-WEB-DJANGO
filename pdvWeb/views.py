from django.shortcuts import render

# Create your views here.
def pdvWeb(request):
    return render(request, 'pdvWeb/pdvWeb.html')