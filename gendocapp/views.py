from django.shortcuts import render
import requests
import os
from django.http import HttpResponse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors
from django.conf import settings

def api(request):
    if request.method == 'GET':
        response = requests.get('https://random-word-api.herokuapp.com/word')
        if response.status_code == 200:
            word = response.json()[0]
        else:
            word = "Error fetching word"
        request.session['random_word'] = word
    else:
        word = request.session.get('random_word', 'Error fetching word')
    
    if request.method == 'POST':
        return string2pdf(word)
    
    return render(request, "home.html", {"word": word})


def index(request):
    return render(request,'home.html')

def string2pdf(string):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

    #textLines = [ 
    #string
    #]

    pdf = canvas.Canvas(response) 
    pdf.setTitle("Test Document")

    pdfmetrics.registerFont( 
    TTFont('abc', os.path.join(settings.BASE_DIR,'static','fonts','times-new-roman.ttf')) 
    )

    pdf.setFont('abc', 36) 
    pdf.drawCentredString(300, 770, "iPAM")

    pdf.setFillColorRGB(0, 0, 0) 
    pdf.setFont("Courier-Bold", 24) 
    pdf.drawCentredString(290, 720, "BE Project") 

    pdf.line(30, 710, 550, 710) 

    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 18) 
    text.setFillColor(colors.black)

    #for line in textLines: 
    #    text.textLine(line) 
    text.textLine(string)

    pdf.drawText(text)

    pdf.showPage()
    pdf.save()

    return response
# Create your views here.
