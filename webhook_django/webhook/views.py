from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        print("POST Data received")
        return HttpResponse("Webhook received!")
