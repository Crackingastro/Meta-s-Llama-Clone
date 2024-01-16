from django.shortcuts import render
import g4f

# Create your views here.

#The Home page is diplayed here 
def chat_gpt(request):
    if request.method == "POST":   
        # getting the input from the user    
        question = request.POST.get("Search")
        
        # Asking g4f the question and fecting the result
        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
        )   

        string = ""

        for message in response:
            string += message

        # Creating a session to store the questions and answers
        qa_pairs = request.session.get('qa_pairs', [])
        qa_pairs.append((question, string))

        request.session['qa_pairs'] = qa_pairs

        return render(request, "main/chat_gpt.html", {"qa_pairs": qa_pairs})
 
    else:
        qa_pairs = request.session.get('qa_pairs', [])
        return render(request,"main/chat_gpt.html", {"qa_pairs": qa_pairs})
