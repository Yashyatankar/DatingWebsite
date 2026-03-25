from django.shortcuts import render


# Create your views here.
def swipping_view(request):
    return render(request, 'swipping.html')