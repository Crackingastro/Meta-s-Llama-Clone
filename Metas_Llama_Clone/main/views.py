from django.shortcuts import render
import requests
from .models import question,answer
from . import creds



# Create your views here.

#The Home page is diplayed here 
def home(response):
    return render(response, "main/home.html", {})

def image_to_text(response):
    return render(response, "main/image_to_text.html", {})

def chat_gpt(response):
    lengths = len(question.objects.all())
    length = []

    for i in range(0,lengths-1):
        length.append(i)

    if response.method == "POST":

        text = response.POST.get("Search")
        x = question(ques = text)
        x.save()

        url = creds.url

        payload = { "message": text}
        headers = creds.headers

        man = requests.post(url, json=payload, headers=headers)

        result = man.json().split("</s>")[0]
        x = answer(ans = result)
        x.save()

        passed_ques = question
        passed_ans = answer

        return render(response, "main/chat_gpt.html", {"length":length, "ques": passed_ques, "ans":passed_ans})
    
    else:
   
        return render(response,"main/chat_gpt.html", {"length":length})
