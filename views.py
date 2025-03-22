# I HAVE CREATED THIS FILE
from django.http import HttpResponse
from django.shortcuts import render
#def index(Request):
    #

#def about(Request):
    #return HttpResponse("about i am  doing study for better future")

def index(Request):
    return render(Request,'index.html')


    #return HttpResponse("Home") 
   
#def ex1(request):
    #sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
            # '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
            # '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             #'''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
   # return HttpResponse((sites))
def analyze(Request):
    #Get the text
    djtext = Request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = Request.GET.get('removepunc','off')
    fullcaps = Request.GET.get('fullcaps','off')
    newlineremover = Request.GET.get('newlineremover','off')
    extraspaceremover = Request.GET.get('extraspaceremover','off')





    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char  in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(Request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(Request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(Request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(Request, 'analyze.html', params)




    

    
       
    else:
        return HttpResponse("Error")   

    


    
    


   
   
   
  
  
  
  
  
  
   

    

   