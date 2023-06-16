# I have created this file - anurag 
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>hello</h1>") 
# -----------------------------------------------------------------------
# CODE FOR VIDEO 6 AND 7

# def about(request):
#     return HttpResponse(" about hello") 

# def whatsapp(request):
#     return HttpResponse('''<h1> whatsapp hello </h1> <a href = https://www.google.com/search?q=whatsapp&oq=whatsapp&aqs=chrome..69i57j69i61j69i60.1532j0j1&sourceid=chrome&ie=UTF-8> WHATSAPP </a> ''') 

# def facebook(request):
#    return HttpResponse('''<h1> facebook hello </h1> <a href = https://www.google.com/search?q=wfacebook&oq=wfacebook&aqs=chrome..69i57.3592j0j1&sourceid=chrome&ie=UTF-8> FACEBOOK </a> ''') 

# def wikipedia(request):
#     return HttpResponse('''<h1> wikipedia hello </h1> <a href = https://www.google.com/search?q=wikipedia&oq=wikipedia&aqs=chrome..69i57j69i60j5.1711j0j1&sourceid=chrome&ie=UTF-8> WIKIPEDIA </a> ''') 

#---------------------------------------------------

# CODE FOR VIDE 7

# def index(request):
#     return HttpResponse('''<h1> HOME </h1>
#                         <a href = "http://127.0.0.1:8000/removepunc"> REMOVE PUNCTUATIONS </a> 
#                         <a href = "http://127.0.0.1:8000/capitalize"> CAPITALIZE </a> 
#                         <a href = "http://127.0.0.1:8000/newlineremove"> NEW LINE REMOVER </a> 
#                         <a href = "http://127.0.0.1:8000/spaceremove"> SPACE REMOVER </a> 
#                         <a href = "http://127.0.0.1:8000/charcount"> CHARACHTER COUNTER </a> 
#                         ''')

# def removepunc(request):
#     djtext = print(request.GET.get('text', 'default'))
#     print(djtext)
#     return HttpResponse('/remove punc')

# def capitalize(request):
#     return HttpResponse('''<h1> CAPITALIZE </h1>
#                         <a href = "/"> HOME </a>''')

# def newlineremove(request):
#     return HttpResponse('''<h1> NEW LINE REMOVE </h1>
#                         <a href = "http://127.0.0.1:8000"> HOME </a>''')

# def spaceremove(request):
#     return HttpResponse('''<h1> SPACE REMOVE </h1>
#                         <a href = "http://127.0.0.1:8000"> HOME </a>''')

# def charcount(request):
#     return HttpResponse('''<h1> CHARACHTER COUNTER </h1>
#                         <a href = "http://127.0.0.1:8000"> HOME </a>''')

#----------------------------------------------------------------------------------------------------------------------
# CODE FOR VID 9

def index(request):
    return render(request, 'index.html')

#----------------------------------------------------------------------------------------------------------------------
# CODE FOR VID 10

def analyze(request):
    
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'default')
    print(removepunc)
    print(djtext)
    
    analyzed = djtext
    
    params = {'purpose' : 'Remove Punctuations', 'analyzed_text': analyzed}
    
    return render(request, 'analyze.html', params)

