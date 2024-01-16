from django.shortcuts import render
import g4f

# Create your views here.

#The Home page is diplayed here 
def home(response):
    return render(response, "main/home.html", {})

def image_to_text(response):
    return render(response, "main/image_to_text.html", {})

def chat_gpt(request):
    if request.method == "POST":       
        question = request.POST.get("Search")

        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
        )   

        string = ""

        for message in response:
            string += message

    
        qa_pairs = request.session.get('qa_pairs', [])
        qa_pairs.append((question, string))

        request.session['qa_pairs'] = qa_pairs

        return render(request, "main/chat_gpt.html", {"qa_pairs": qa_pairs})
 
    else:
        qa_pairs = request.session.get('qa_pairs', [])
        return render(request,"main/chat_gpt.html", {"qa_pairs": qa_pairs})
