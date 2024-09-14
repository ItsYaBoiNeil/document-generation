from django.shortcuts import render
import requests
import os
from django.http import HttpResponse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors
from django.conf import settings

# def api(request):
#     if request.method == 'GET':
#         response = requests.get('https://random-word-api.herokuapp.com/word')
#         if response.status_code == 200:
#             word = response.json()[0]
#         else:
#             word = "Error fetching word"
#         request.session['random_word'] = word
#     else:
#         word = request.session.get('random_word', 'Error fetching word')
    
#     if request.method == 'POST':
#         return string2pdf(word)
    
#     return render(request, "home.html", {"word": word})


# def index(request):
#     return render(request,'home.html')

# def string2pdf(string):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

#     #textLines = [ 
#     #string
#     #]

#     pdf = canvas.Canvas(response) 
#     pdf.setTitle("Test Document")

#     pdfmetrics.registerFont( 
#     TTFont('abc', os.path.join(settings.BASE_DIR,'static','fonts','times-new-roman.ttf')) 
#     )

#     pdf.setFont('abc', 36) 
#     pdf.drawCentredString(300, 770, "iPAM")

#     pdf.setFillColorRGB(0, 0, 0) 
#     pdf.setFont("Courier-Bold", 24) 
#     pdf.drawCentredString(290, 720, "BE Project") 

#     pdf.line(30, 710, 550, 710) 

#     text = pdf.beginText(40, 680) 
#     text.setFont("Courier", 18) 
#     text.setFillColor(colors.black)

#     #for line in textLines: 
#     #    text.textLine(line) 
#     text.textLine(string)

#     pdf.drawText(text)

#     pdf.showPage()
#     pdf.save()

#     return response
# Create your views here.


import os
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors
from django.conf import settings
from mistralai import Mistral
import textwrap

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


# Fetch data from Mistral LLM
def fetch_llm_response():
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        return "API key not found. Set the environment variable 'MISTRAL_API_KEY'."
    
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    
    try:
        # Making a request to Mistral LLM to get the planets of our solar system
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Name the planets of our solar system",
                },
            ]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error fetching LLM response: {e}"

# Django view to fetch and show the response from Mistral LLM
def api(request):
    if request.method == 'GET':
        word = fetch_llm_response()
        request.session['llm_response'] = word
    else:
        word = request.session.get('llm_response', 'Error fetching LLM response')
    
    if request.method == 'POST':
        return string2pdf(word)
    
    return render(request, "home.html", {"word": word})

# Function to generate PDF from string
import textwrap

def string2pdf(string):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="llm_response.pdf"'

    pdf = canvas.Canvas(response)
    pdf.setTitle("LLM Response Document")

    pdfmetrics.registerFont(
        TTFont('abc', os.path.join(settings.BASE_DIR, 'static', 'fonts', 'times-new-roman.ttf'))
    )

    pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, "LLM Response")

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, "Solar System Planets")

    pdf.line(30, 710, 550, 710)

    # Define the maximum width and margin
    max_width = 500
    margin = 40
    text = pdf.beginText(margin, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.black)

    # Wrap text to fit within the specified width
    wrapped_text = textwrap.fill(string, width=60)  # Adjust width as needed

    # Add each line of wrapped text to the PDF
    for line in wrapped_text.split('\n'):
        text.textLine(line)

    pdf.drawText(text)
    pdf.showPage()
    pdf.save()

    return response

