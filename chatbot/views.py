from django.shortcuts import render

import spacy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .nlp import process_text 

@csrf_exempt

# def chatbot(request):
    
#     if request.method == 'POST':
#         text = request.POST.get('text', '')
#          # Utilisez le modèle spaCy pour traiter le texte et renvoyer une réponse
         
#         response = "Bonjour, comment puis-je vous aider ?"
#         return JsonResponse({'response': response})
    
    
# from django.shortcuts import render
# from chatbot.chatbot import get_response

def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST['question']
        response = "Bonjour, comment puis-je vous aider ?"
        return render(request, 'chatbot.html', {'question': question, 'response': response})
    else:
        return render(request, 'chatbot.html')




# # Create your views here.
# @csrf_exempt
# def chatbot_view(request):
#      if request.method == "POST":
#          data = json.load (request.body) 
#          text = data.get("text")
#          response = process_text(text)
#          return JsonResponse({"response": response})
#      return JsonResponse({"error": "Invalid request"}) 